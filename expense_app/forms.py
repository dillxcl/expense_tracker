from django import forms
from .models import Year_Expense, Daily_Expense
from django.contrib.auth.models import User

class YearExpenseForm(forms.ModelForm):
    class Meta:
        model = Year_Expense
        fields = ["year", "annual_salary"]
        exclude = ['user']


class DailyExpenseForm(forms.ModelForm):
    class Meta:
        model = Daily_Expense
        fields = ['category', 'daily_spent', 'date_input']