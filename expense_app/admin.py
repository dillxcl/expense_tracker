from django.contrib import admin
from .models import Year_Expense, Month_Expense, Daily_Expense
# Register your models here.

admin.site.register(Year_Expense)
admin.site.register(Month_Expense)
admin.site.register(Daily_Expense)