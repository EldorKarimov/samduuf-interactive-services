from django.urls import path
from .views import StudentRegisterView, LoginView, LogoutView

urlpatterns = [
    path('signup/', StudentRegisterView.as_view(), name="student_register"),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]