from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Year_Expense(models.Model):
    # name - What Year (front end option to select what year)
    # budget - annual salary
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    year = models.CharField(max_length=100)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.year

class Month_Expense(models.Model):
    # name - Month (auto generate 12 months)
    # year_expense = models.ForiegnKey(Year_Expense, on_delete=models.CASCADE)
    pass

class Daily_Expense(models.Model):
    # category - which items I have spent on 
    # spent - which much money you have spent
    pass