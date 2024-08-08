from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve 


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('i18n/', include('django.conf.urls.i18n')),
    path('hacktivist/', admin.site.urls),
] 

urlpatterns += i18n_patterns(
    path('account/', include('accounts.urls')),
    path('', include('main.urls')),
)