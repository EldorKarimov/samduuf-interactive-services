from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Leader, Appeal, Answer
from .forms import AppealForm, AnswerForm
from accounts.permissions import CustomLoginRequiredMixin

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
            form_create.student = request.user
            form_create.save()
            return redirect('home')
        else:
            context = {
                'form':form
            }
            return render(request, 'appeal.html', context)
        
class AppealListDetailView(CustomLoginRequiredMixin, View):
    def get(self, request, student_id=None):
        if student_id is None:
            appeals = Appeal.objects.filter(leader__leader__username=request.user.username)
            context = {
                'appeals':appeals
            }
            return render(request, 'appeal_list.html', context)
        else:
            form = AnswerForm()
            context = {
                'form':form
            }
            return render(request, 'appeal_detail.html', context)
    def post(self, request, student_id):
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            print(student_id)
            form_create = form.save(commit=False)
            form_create.leader = request.user.get_full_name
            form_create.student_id = student_id
            form_create.save()
            return redirect('appeal_list')
        else:
            form = AnswerForm(data=request.POST)
            context = {
                'form':form
            }
            return render(request, 'appeal_detail.html', context)
