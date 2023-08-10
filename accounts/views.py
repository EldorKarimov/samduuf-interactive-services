from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import LeaderProfileUpdateForm, StudentRegisterForm, CustomPasswordChangeForm
from .models import Student
from django.http import HttpResponse
from .api import HemisApi
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import CustomLoginRequiredMixin
from django.utils.translation import gettext_lazy as _

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})
    def post(self, request):

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                login(request, user)
                return redirect('appeal_list')
            else:
                login(request, user)
                return redirect('home')
        else:
            messages.info(request, _("username yoki parol xato!"))
            return render(request, 'signin.html', {'form': form})
        
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home')

class StudentRegisterView(View, HemisApi):
    def get(self, request):
        form = StudentRegisterForm()
        context = {
            'form':form
        }
        return render(request, 'signup.html', context)
    def post(self, request):
        form = StudentRegisterForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        student = Student.objects.filter(username=username)
        err = self.user_data_json(username, password)
        if student.exists() and err != 'error':
            messages.error(request, _('Bunday foydalanuvchi allaqachon mavjud!'))
            return redirect('student_register')
        if self.user_data_json(username, password) == 'error':
            messages.error(request, _("id yoki parol xato! Iltimos tekshirib qaytadan kiriting."))
            return redirect('student_register')
        else:
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                context = {
                    'form':form
                }
                return render(request, 'signup.html', context)
            
class ProfileDataView(LoginRequiredMixin, View):
    def get(self, request):
        student = Student.objects.get(username = request.user.username)
        context = {
            'student':student
        }
        return render(request, 'profile-data.html', context)

class EduDataView(LoginRequiredMixin, View):
    def get(self, request):
        student = Student.objects.get(username=request.user.username)
        context = {
            'student':student
        }
        return render(request, 'edu-data.html', context)
    
class LeaderProfileView(CustomLoginRequiredMixin, View):
    def get(self, request):
        leader = Student.objects.get(username = request.user.username)
        form = LeaderProfileUpdateForm(instance=leader)
        context = {
            'form':form
        }
        return render(request, 'leader_profile.html', context)
    
    def post(self, request):
        leader = Student.objects.get(username = request.user.username)
        form = LeaderProfileUpdateForm(data=request.POST, instance=leader)
        if form.is_valid():
            form.save()
            messages.success(request, _("Ma'lumot muvaffaqqiyatli o'zgartirildi."))
            return redirect('profile_leader')
        else:
            context = {
                'form':form
            }
            return render(request, 'leader_profile.html', context)
        
class PasswordChangeView(CustomLoginRequiredMixin, View):
    def get(self, request):
        form = CustomPasswordChangeForm(user=request.user)
        context = {
            'form':form
        }
        return render(request, 'password_change.html', context)
    
    def post(self, request):
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('password_change_done')
        else:
            context = {
                'form':form
            }
            return render(request, 'password_change.html', context)
        
def password_change_done(request):
    return render(request, 'password_change_done.html')