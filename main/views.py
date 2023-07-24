from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Leader, Appeal, Answer
from .forms import AppealForm, AnswerForm

class HomePageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home.html')
    
class AppealView(LoginRequiredMixin, View):
    def get(self, request):
        form = AppealForm()
        context = {
            'form':form
        }
        return render(request, 'appeal.html', context)
    def post(self, request):
        form = AppealForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form_create = form.save(commit=False)
            form_create.student_id = request.user.student_id_number
            form_create.faculty = request.user.faculty
            form_create.eduForm = request.user.eduForm
            form_create.specialty = request.user.specialty
            form_create.group = request.user.group
            form_create.full_name = request.user.full_name
            form_create.phone = request.user.phone
            form_create.save()
            return redirect('home')
        else:
            context = {
                'form':form
            }
            return render(request, 'appeal.html', context)
        
class AnswerView(LoginRequiredMixin, View):
    def get(self, request, student_id=None):
        if student_id is not None:
            form = AnswerForm()
            context = {
                'form':form
            }
            return render(request, 'appeal_detail.html', context)
        else:
            appeals = Appeal.objects.all()
            context = {
                'appeals':appeals
            }
            return render(request, 'appeal_list.html', context)