from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import Leader, Appeal, Answer
from .forms import AppealForm, AnswerForm
from accounts.permissions import CustomLoginRequiredMixin, CustomStudentLoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

def custom_403(request, exeption):
    return render(request, '403.html', status=403)

def custom_404(request, exeption):
    return render(request, '404.html', status=404)

class HomePageView(View):
    def get(self, request):
        appeal_count = Appeal.objects.count()
        answer_count = Answer.objects.count()
        appeal_in_process = appeal_count - answer_count
        context = {
            'appeal_count':appeal_count,
            'answer_count':answer_count,
            'appeal_in_process':appeal_in_process
        }
        return render(request, 'home.html', context)
    

class AllServicesView(CustomStudentLoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'all-services.html')
    
class AppealToLeaderView(CustomStudentLoginRequiredMixin, View):
    def get(self, request):
        form = AppealForm()
        leaders = Leader.objects.all()
        context = {
            'form':form,
            'leaders':leaders
        }
        return render(request, 'appeal-to-leader.html', context)
    
    def post(self, request):
        form = AppealForm(data=request.POST, files=request.FILES)
        print('after validate')
        if form.is_valid():
            print('before validate')
            form_create = form.save(commit=False)
            form_create.student = request.user
            form_create.save()
            messages.success(request, _("Murojaat muvaffaqqiyatli yuborildi."))
            return redirect('appeal_to_leader')
        else:
            context = {
                'form':form
            }
            return render(request, 'appeal-to-leader.html', context)
    

class MyApplicationView(CustomStudentLoginRequiredMixin, View):
    def get(self, request):
        appeals = Appeal.objects.filter(student__username = request.user.username).order_by('-created_at')
        context = {
            'appeals':appeals
        }
        return render(request, 'my-application-list.html', context)
    
class MyAnswerView(CustomStudentLoginRequiredMixin, View):
    def get(self, request):
        answers = Answer.objects.filter(student_id=request.user.username)
        context = {
            'answers':answers
        }
        return render(request, 'my-answers.html', context)
    
    
class AppealListDetailView(CustomLoginRequiredMixin, View):
    def get(self, request, appeal_id=None):
        if appeal_id is None:
            appeals = Appeal.objects.filter(leader__leader__username=request.user.username).order_by('-created_at')
            paginator = Paginator(appeals, 20)
            page_num = request.GET.get('page')
            page_obj = paginator.get_page(page_num)

            context = {
                'appeals':page_obj
            }
            return render(request, 'appeal_list.html', context)
        else:
            form = AnswerForm()
            appeal_student = Appeal.objects.get(id=appeal_id)
            context = {
                'form':form,
                'appeal_student':appeal_student
            }
            return render(request, 'appeal_detail.html', context)
    def post(self, request, appeal_id):
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            appeal = get_object_or_404(Appeal, id=appeal_id)
            form_create = form.save(commit=False)
            form_create.leader = str(request.user.first_name) + str(request.user.last_name)
            form_create.student_id = appeal.student.student_id_number
            form_create.save()
            messages.success(request, _("Javob muvaffaqqiyatli saqlandi."))
            return redirect('appeal_list')
        else:
            form = AnswerForm(data=request.POST)
            context = {
                'form':form
            }
            return render(request, 'appeal_detail.html', context)
