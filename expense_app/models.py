from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Year_Expense(models.Model):
    # name - What Year (front end option to select what year)
    # budget - annual salary
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    year = models.CharField(max_length=100)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.year

    def monthly_salary(self):
        month_average = self.annual_salary/12
        return round(month_average,2)
        


class Month_Expense(models.Model):
    year = models.ForeignKey(Year_Expense, on_delete=models.CASCADE, default='', null=True)
    month = models.CharField(max_length=100, default='')
    # year_expense = models.ForiegnKey(Year_Expense, on_delete=models.CASCADE)
    def __str__(self):
        return self.month
@receiver(post_save, sender=Year_Expense)
def create_month(sender, instance, created, **kwargs):
    if created:
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        for month in months:
            Month_Expense.objects.create(year=instance, month=month)
  


class Daily_Expense(models.Model):
    # category - which items I have spent on 
    # spent - which much money you have spent
    pass