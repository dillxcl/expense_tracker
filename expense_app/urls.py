from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_home, name='home'),
]
