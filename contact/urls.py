from django.urls import include ,path 
from django.contrib import admin
from contact import views

urlpatterns = [
    path('', views.home, name='contact'),
]