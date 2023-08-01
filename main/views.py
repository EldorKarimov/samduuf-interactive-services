from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Leader, Appeal, Answer
from .forms import AppealForm, AnswerForm
from accounts.permissions import CustomLoginRequiredMixin
from django.contrib import messages

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
    
# class AppealView(LoginRequiredMixin, View):
#     def get(self, request):
#         form = AppealForm()
#         context = {
#             'form':form
#         }
#         return render(request, 'appeal.html', context)
#     def post(self, request):
#         form = AppealForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form_create = form.save(commit=False)
#             form_create.student = request.user
#             form_create.save()
#             return redirect('home')
#         else:
#             context = {
#                 'form':form
#             }
#             return render(request, 'appeal.html', context)
        
# class AppealListDetailView(CustomLoginRequiredMixin, View):
#     def get(self, request, appeal_id=None):
#         if appeal_id is None:
#             appeals = Appeal.objects.filter(leader__leader__username=request.user.username)
#             context = {
#                 'appeals':appeals
#             }
#             return render(request, 'appeal_list.html', context)
#         else:
#             form = AnswerForm()
#             appeal_student = Appeal.objects.get(id=appeal_id)
#             context = {
#                 'form':form,
#                 'appeal_student':appeal_student
#             }
#             return render(request, 'appeal_detail.html', context)
#     def post(self, request, appeal_id):
#         form = AnswerForm(data=request.POST)
#         if form.is_valid():
#             appeal = Appeal.objects.get(id=appeal_id)
#             form_create = form.save(commit=False)
#             form_create.leader = request.user.get_full_name
#             form_create.student_id = appeal.student.student_id_number
#             form_create.save()
#             return redirect('appeal_list')
#         else:
#             form = AnswerForm(data=request.POST)
#             context = {
#                 'form':form
#             }
#             return render(request, 'appeal_detail.html', context)
