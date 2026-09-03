from django.shortcuts import render
from django.views import View

def home(request):
    return render(request, 'dashboard/home.html')

def reports(request, report_type):
    return render(request, 'dashboard/reports.html', {'report_type': report_type})

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard/home.html')
