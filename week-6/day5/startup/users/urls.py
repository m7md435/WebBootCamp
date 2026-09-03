from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile-cbv/<str:username>/', views.UserProfileView.as_view(), name='profile-cbv'),
]
