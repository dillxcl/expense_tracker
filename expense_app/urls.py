from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_home, name='home'),
    path('year_expense_delete/<year_expense_id>', views.year_expense_delete, name='year_expense_delete')
]
