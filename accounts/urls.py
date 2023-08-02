from django.urls import path
from .views import (
    StudentRegisterView, LoginView, 
    LogoutView, ProfileDataView,
    EduDataView
)

urlpatterns = [
    path('signup/', StudentRegisterView.as_view(), name="student_register"),
    path('signin/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/index', ProfileDataView.as_view(), name='profile_data'),
    path('profile/edu/data/', EduDataView.as_view(), name="edu_data")
]