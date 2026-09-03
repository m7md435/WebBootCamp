from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def about(request):
	return render(request, 'about.html')


def contact(request):
	return render(request, 'contact.html')


def custom_404(request, exception):
	from django.http import HttpResponseNotFound
	return HttpResponseNotFound('404: Page not found')
