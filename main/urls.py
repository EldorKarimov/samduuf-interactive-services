from django.urls import path
from .views import (
    HomePageView, AllServicesView, AppealToLeaderView, MyApplicationView, AppealListDetailView,
    deleteAppeal
) 

handler403 = 'main.views.custom_403'
handler404 = 'main.views.custom_404'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('service/all', AllServicesView.as_view(), name='all_services'),
    path('appeal-to-leader/', AppealToLeaderView.as_view(), name='appeal_to_leader'),
    path('my/application/list/', MyApplicationView.as_view(), name='application_list'),
    path('appeal/list/', AppealListDetailView.as_view(), name='appeal_list'),
    path('appeal/detail/<int:appeal_id>/', AppealListDetailView.as_view(), name='appeal_detail'),
    path('appeal/delete/<int:appeal_id>/', deleteAppeal, name='appeal_delete')
]