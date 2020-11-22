from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Year_Expense, Month_Expense
from .forms import YearExpenseForm


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



def expense_month(request, year_expense_id):
    year_expense = Year_Expense.objects.get(pk=year_expense_id)
    month_expense = Month_Expense.objects.filter(year=year_expense)
    print(month_expense)
    return render(request, 'expense_month.html', {'month_expense': month_expense, 'year_expense': year_expense})