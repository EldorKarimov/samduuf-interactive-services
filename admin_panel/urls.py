from django.urls import path
from .views import AdminPage

urlpatterns = [
    path('', AdminPage.as_view(), name='admin_page')
]