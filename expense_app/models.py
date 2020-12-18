from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from django.template.defaultfilters import slugify
import datetime
# Create your models here.

class Year_Expense(models.Model):
    # name - What Year (front end option to select what year)
    # budget - annual salary
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    year = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    year_slug = models.SlugField(max_length=200, unique=True, default='')
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        super(Year_Expense, self).save(*args, **kwargs)
        if not self.year_slug:
            self.year_slug = slugify(self.year) + "%" + str(self.id)
            self.save()

    def __str__(self):
        return self.year

    def total_income(self):
        total_income+=self.annual_salary
        return total_income
        
    def monthly_salary(self):
        month_average = self.annual_salary/12
        return round(month_average,2)
        
    def money_left(self):
        each_money_left = Month_Expense.objects.filter(year=self)
        total_expense_left = 0
        for each_expense in each_money_left:
            total_expense_left += each_expense.monthly_expense_left()
        if round(total_expense_left) >= self.annual_salary:
            return self.annual_salary
        else:
            return total_expense_left

class Month_Expense(models.Model):
    year = models.ForeignKey(Year_Expense, on_delete=models.CASCADE, default='', null=True)
    month = models.CharField(max_length=100, default='')
    month_slug = models.SlugField(max_length=200, unique=True, default='')
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0))
    # year_expense = models.ForiegnKey(Year_Expense, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super(Month_Expense, self).save(*args, **kwargs)
        if not self.month_slug:
            self.month_slug = slugify(self.month) + "%" + str(self.id)
            self.save()

    def __str__(self):
        return self.month

    def monthly_expense_left(self):
        daily_expense = Daily_Expense.objects.filter(month=self)
        total_expense_amount = 0
        for each_expense in daily_expense:
            total_expense_amount += each_expense.daily_spent
        return self.monthly_salary - total_expense_amount

    def monthly_total_transactions(self):
        daily_expense = Daily_Expense.objects.filter(month=self)
        return len(daily_expense)
        
@receiver(post_save, sender=Year_Expense)
def create_month(sender, instance, created, **kwargs):
    if created:
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        monthly_salary = instance.annual_salary/12
        for month in months:
            Month_Expense.objects.create(year=instance, month=month, monthly_salary=monthly_salary)
  


class Daily_Expense(models.Model):
    month = models.ForeignKey(Month_Expense, on_delete=models.CASCADE, default='', null=True)
    category = models.CharField(max_length=100, default='')
    daily_spent = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0))
    date_input = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.date_input

