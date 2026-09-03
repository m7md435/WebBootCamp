from django.shortcuts import render
from django.views import View

def list(request):
    return render(request, 'courses/list.html')

def detail(request, slug):
    return render(request, 'courses/detail.html', {'slug': slug})

def category(request, category):
    return render(request, 'courses/category.html', {'category': category})

class CourseListView(View):
    def get(self, request):
        return render(request, 'courses/list.html')
