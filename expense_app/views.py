from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Year_Expense, Month_Expense, Daily_Expense
from .forms import YearExpenseForm, DailyExpenseForm


# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def expense_home(request):
    if request.method == 'POST':
        form = YearExpenseForm(request.POST)
        print(form)
        if form.is_valid():
            year_expense_model = form.save(commit=False)
            year_expense_model.user = request.user 
            year_expense_model.save()
            year_expense = Year_Expense.objects.filter(user=request.user)
            return render(request, 'expense_home.html', {'year_expense': year_expense})
        else:
            return redirect('home')
    else:
        year_expense = Year_Expense.objects.filter(user=request.user)
        return render(request, 'expense_home.html', {'year_expense':year_expense})


@login_required(login_url='login')
def year_expense_delete(request, year_expense_id):
    year_expense = Year_Expense.objects.get(pk=year_expense_id)
    year_expense.delete()
    return redirect('home')


@login_required(login_url='login')
def expense_month(request, year_expense_id):
    year_expense = Year_Expense.objects.get(pk=year_expense_id)
    month_expense = Month_Expense.objects.filter(year=year_expense)
    return render(request, 'expense_month.html', {'month_expense': month_expense, 'year_expense': year_expense})


@login_required(login_url='login')
def expense_daily(request, month_expense_id):
    if request.method == 'POST':
        form = DailyExpenseForm(request.POST)
        if form.is_valid():
            current_month = Month_Expense.objects.get(pk=month_expense_id)
            daily_expense_model = form.save(commit=False)
            daily_expense_model.month = current_month
            daily_expense_model.save()
            daily_expense = Daily_Expense.objects.filter(month=current_month)
            return render(request, 'expense_daily.html', {'month_expense':current_month, 'daily_expense': daily_expense})
        else:
            return HttpResponseRedirect(request.path_info)
    
    current_month = Month_Expense.objects.get(pk=month_expense_id)
    daily_expense = Daily_Expense.objects.filter(month=current_month)
    return render(request, 'expense_daily.html', {'month_expense':current_month, 'daily_expense': daily_expense})


@login_required(login_url='login')
def daily_expense_delete(request, month_expense_id , daily_expense_id):
    daily_expense = Daily_Expense.objects.get(pk=daily_expense_id)
    daily_expense.delete()
    current_month = Month_Expense.objects.get(pk=month_expense_id)
    daily_expense = Daily_Expense.objects.filter(month=current_month)
    return render(request, 'expense_daily.html', {'month_expense':current_month, 'daily_expense': daily_expense})