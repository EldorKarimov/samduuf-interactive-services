from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Leader, Appeal, Answer
from .forms import AppealForm, AnswerForm
from accounts.permissions import CustomLoginRequiredMixin
from django.contrib import messages
from accounts.api import HemisApi

def custom_403(request, exeption):
    return render(request, '403.html', status=403)

def custom_404(request, exeption):
    return render(request, '404.html', status=404)

class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')

class AllServicesView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'all-services.html')
    
class AppealToLeaderView(LoginRequiredMixin, View):
    def get(self, request):
        form = AppealForm()
        context = {
            'form':form
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
            messages.success(request, "Murojaat muvaffaqqiyatli yuborildi.")
            return redirect('appeal_to_leader')
        else:
            context = {
                'form':form
            }
            return render(request, 'appeal-to-leader.html', context)
    

class MyApplicationView(LoginRequiredMixin, View):
    def get(self, request):
        appeals = Appeal.objects.filter(student__username = request.user.username).order_by('-created_at')
        context = {
            'appeals':appeals
        }
        return render(request, 'my-application-list.html', context)
    
    
class AppealListDetailView(CustomLoginRequiredMixin, View):
    def get(self, request, appeal_id=None):
        if appeal_id is None:
            appeals = Appeal.objects.filter(leader__leader__username=request.user.username)
            context = {
                'appeals':appeals
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
            form_create.leader = request.user.get_full_name
            form_create.student_id = appeal.student.student_id_number
            form_create.save()
            return redirect('appeal_list')
        else:
            form = AnswerForm(data=request.POST)
            context = {
                'form':form
            }
            return render(request, 'appeal_detail.html', context)
        

def deleteAppeal(request, appeal_id):
    appeal = get_object_or_404(Appeal, id=appeal_id)
    appeal.delete()
    return redirect('appeal_list')