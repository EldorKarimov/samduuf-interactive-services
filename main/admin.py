from django.contrib import admin

from .models import Leader, Appeal, Answer, RentalHouse

admin.site.register([Appeal, Answer, RentalHouse])

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    search_fields = ['leader__first_name', 'leader__last_name']