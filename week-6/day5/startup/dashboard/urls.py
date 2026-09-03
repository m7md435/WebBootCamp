from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='home'),
    path('home/', views.home, name='fbv-home'),
    path('reports/<str:report_type>/', views.reports, name='reports'),
]
