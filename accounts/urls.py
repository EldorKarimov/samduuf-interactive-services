from django.urls import path
from .views import (
    StudentRegisterView, LoginView, 
    LogoutView, ProfileDataView,
    EduDataView, LeaderProfileView, 
    PasswordChangeView
)
from .views import password_change_done

urlpatterns = [
    path('signup/', StudentRegisterView.as_view(), name="student_register"),
    path('signin/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/index', ProfileDataView.as_view(), name='profile_data'),
    path('profile/edu/data/', EduDataView.as_view(), name="edu_data"),
    path('profile/leader/', LeaderProfileView.as_view(), name="profile_leader"),
    path('password/change/', PasswordChangeView.as_view(), name="password_change"),
    path('password/change/done/', password_change_done, name="password_change_done"),
]