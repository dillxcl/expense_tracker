from django import forms
from .models import Year_Expense
from django.contrib.auth.models import User

class YearExpenseForm(forms.ModelForm):
    class Meta:
        model = Year_Expense
        fields = ["year", "annual_salary"]
        exclude = ['user']
