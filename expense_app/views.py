from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Year_Expense, Month_Expense, Daily_Expense
from .forms import YearExpenseForm, DailyExpenseForm
import json
import datetime
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def expense_home(request):
    if request.method == 'POST':
        form = YearExpenseForm(request.POST)
        if form.is_valid():
            year_expense_model = form.save(commit=False)
            year_expense_model.user = request.user 
            year_expense_model.save()
            year_expense = Year_Expense.objects.filter(user=request.user)
            total_income = year_total_income(year_expense)
            year_income = current_year_income(year_expense)
            context = {
            'year_expense':year_expense, 
            'total_income':total_income,
            'current_year_income': year_income
                }
            return render(request, 'expense_home.html', context)
        else:
            return redirect('home')
    else:
        year_expense = Year_Expense.objects.filter(user=request.user)
        total_income = year_total_income(year_expense)
        year_income = current_year_income(year_expense)
        context = {
            'year_expense':year_expense, 
            'total_income':total_income,
            'current_year_income': year_income
            }
        return render(request, 'expense_home.html', context)

def year_total_income(year_expense):
    total_income = 0
    for each_year in year_expense:
        total_income += each_year.annual_salary
    return total_income

def current_year_income(year_expense):
    res_income = 0
    for each_year in year_expense:
        print(each_year.year)
        if str(each_year.year) == str(datetime.date.today().year):
            res_income = each_year.annual_salary
    return res_income
    





@login_required(login_url='login')
def year_expense_delete(request, year_expense_id):
    year_expense = Year_Expense.objects.get(pk=year_expense_id)
    year_expense.delete()
    return redirect('home')


@login_required(login_url='login')
def expense_month(request, year_slug):
    year_expense = get_object_or_404(Year_Expense, year_slug=year_slug)
    month_expense = Month_Expense.objects.filter(year=year_expense)
    return render(request, 'expense_month.html', {'month_expense': month_expense, 'year_expense': year_expense})


@login_required(login_url='login')
def expense_daily(request, year_slug, month_slug):
    current_month = Month_Expense.objects.get(month_slug=month_slug)
    daily_expense = Daily_Expense.objects.filter(month=current_month)
    if request.method == 'DELETE':
        id = json.loads(request.body)['id']
        expense = get_object_or_404(Daily_Expense, pk=id)
        expense.delete()
        return render(request, 'expense_daily.html', {'month_expense':current_month, 'daily_expense': daily_expense})
    return render(request, 'expense_daily.html', {'month_expense':current_month, 'daily_expense': daily_expense})

def create_daily_expense(request):
    if request.method == 'POST':
        month_id= request.POST['month_id']
        daily_id = request.POST['daily_id']
        category = request.POST['category']
        daily_spent = request.POST['expense']
        date_input = request.POST['date']
        current_month = Month_Expense.objects.get(pk=month_id)
        if daily_id == "None":
            Daily_Expense.objects.create(month=current_month, category=category, daily_spent=daily_spent, date_input=date_input)
        else:
            Daily_Expense.objects.filter(pk=daily_id).update(category=category,daily_spent=daily_spent,date_input=date_input)
        return HttpResponse('')

@login_required(login_url='login')
def daily_expense_delete(request, month_expense_id , daily_expense_id):
    daily_expense = Daily_Expense.objects.get(pk=daily_expense_id)
    daily_expense.delete()
    current_month = Month_Expense.objects.get(pk=month_expense_id)
    daily_expense = Daily_Expense.objects.filter(month=current_month)
    return render(request, 'expense_daily.html', {'month_expense':current_month, 'daily_expense': daily_expense})


def home_test(request):
    return render(request, 'expense_test.html', {})
