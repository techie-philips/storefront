from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcome_page(request):
    return HttpResponse(f'Welcome to django')


def about_page(request):
    return HttpResponse('about page')
