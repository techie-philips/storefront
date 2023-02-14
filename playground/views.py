from django.shortcuts import render
import django

# Create your views here.


def welcome_page(request):
    user = 'John Doe'
    return django.http.HttpResponse(f'Welcome, {user}! this is django')
