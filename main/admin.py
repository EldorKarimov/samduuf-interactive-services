from django.contrib import admin

from .models import Leader, Appeal, Answer

admin.site.register([Appeal, Answer])

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    search_fields = ['leader__first_name', 'leader__last_name']