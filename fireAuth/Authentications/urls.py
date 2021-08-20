from os import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('singIn', views.signIn, name='signIn'),
    path('addUser', views.addUser, name='addUser')
]