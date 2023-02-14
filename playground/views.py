from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcome_page(request):
	message = "Welcome to Django"
	return render(request, 'home.html', context={'message': message})


def about_page(request):
	return HttpResponse('about page')
