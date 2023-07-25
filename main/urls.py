from django.urls import path
from .views import HomePageView, AppealView, AppealListDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('appeal/', AppealView.as_view(), name="appeal"),
    path('appeal-list/', AppealListDetailView.as_view(), name='appeal_list'),
    path('appeal-detail/<str:student_id>/', AppealListDetailView.as_view(), name='appeal_detail'),
]