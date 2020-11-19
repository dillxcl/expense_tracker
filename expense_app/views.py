from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def expense_home(request):
    return render(request, 'expense_home.html', {})



