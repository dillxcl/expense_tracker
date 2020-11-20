from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Year_Expense
from .forms import YearExpenseForm


# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def expense_home(request):
    if request.method == 'POST':
        form = YearExpenseForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            year_expense = Year_Expense.objects.all()
            return render(request, 'expense_home.html', {'year_expense': year_expense})
        else:
            return redirect('home')
    else:
        year_expense = Year_Expense.objects.all()
        return render(request, 'expense_home.html', {'year_expense':year_expense})



def year_expense_delete(request, year_expense_id):
    year_expense = Year_Expense.objects.get(pk=year_expense_id)
    year_expense.delete()
    return redirect('home')