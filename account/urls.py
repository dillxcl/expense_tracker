from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', views.log_out, name='logout'),
]
