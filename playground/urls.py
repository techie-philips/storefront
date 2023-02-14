from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page),
    path('about/', views.about_page)
]
