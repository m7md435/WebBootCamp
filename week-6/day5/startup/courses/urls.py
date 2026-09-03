from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='cbv-list'),
    path('list/', views.list, name='list'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('category/<str:category>/', views.category, name='category'),
]
