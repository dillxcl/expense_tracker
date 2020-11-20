from django import forms
from .models import Year_Expense

class YearExpenseForm(forms.ModelForm):
    class Meta:
        model = Year_Expense
        fields = ["year", "annual_salary"]