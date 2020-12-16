from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #Expense_home page
    path('expense_home', views.expense_home, name='home'),
    path('year_expense_delete/<year_expense_id>', views.year_expense_delete, name='year_expense_delete'),

    #Display Expense_month page
    path('expense_home/<year_slug>', views.expense_month, name='expense_month'),
    
    #Expense_Daily page
    path('expense_home/<year_slug>/<month_slug>', views.expense_daily, name='expense_daily'),
    path('expense_home/daily_expense_create/', views.create_daily_expense, name='daily_expense_create'),
    path('expense_daily/<month_expense_id>/<daily_expense_id>', views.daily_expense_delete, name='daily_expense_delete'),

    path('home_test', views.home_test, name='home_test')
]
