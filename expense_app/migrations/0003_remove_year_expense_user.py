# Generated by Django 3.0.6 on 2020-11-20 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0002_year_expense_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year_expense',
            name='user',
        ),
    ]