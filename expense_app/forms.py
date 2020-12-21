from django import forms
from .models import Year_Expense, Daily_Expense
from django.contrib.auth.models import User

class YearExpenseForm(forms.Form):
    
    pk = forms.IntegerField()
    year = forms.CharField()
    annual_salary = forms.DecimalField()
        
class DailyExpenseForm(forms.ModelForm):
    class Meta:
        model = Daily_Expense
        fields = ['category', 'daily_spent', 'date_input']