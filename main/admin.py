from django.contrib import admin

from .models import Leader, Appeal, Answer

admin.site.register([Leader, Appeal, Answer])


    