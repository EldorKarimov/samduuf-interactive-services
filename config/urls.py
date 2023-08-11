from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
] 

urlpatterns += i18n_patterns(
    path('account/', include('accounts.urls')),
    path('', include('main.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)