from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import StudentRegisterForm
from .models import Student
from django.http import HttpResponse
from .api import HemisApi
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin



class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})
    def post(self, request):

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "username or password error!")
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
            messages.error(request, 'This user already exis!')
            return redirect('student_register')
        if self.user_data_json(username, password) == 'error':
            messages.error(request, "id yoki parol xato! Iltimos tekshirib qaytadan kiriting.")
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