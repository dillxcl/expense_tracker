# Generated by Django 3.0.6 on 2020-11-24 23:02

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0010_remove_month_expense_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_expense',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='daily_expense',
            name='daily_spent',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
        migrations.AddField(
            model_name='daily_expense',
            name='date_input',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='daily_expense',
            name='month',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='expense_app.Month_Expense'),
        ),
    ]
