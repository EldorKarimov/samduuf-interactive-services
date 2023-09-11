from django.shortcuts import render
from django.views import View

class AdminPage(View):
    def get(self, request):
        return render(request, 'admin.html')