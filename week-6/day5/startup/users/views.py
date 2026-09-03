from django.shortcuts import render
from django.views import View

def login(request):
    return render(request, 'users/login.html')

def profile(request, username):
    return render(request, 'users/profile.html', {'username': username})

class UserProfileView(View):
    def get(self, request, username):
        return render(request, 'users/profile.html', {'username': username})
