# Generated by Django 4.0.6 on 2023-01-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_schedule_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockschedulemanager',
            name='date',
            field=models.TextField(default='2023-01-15', unique=True),
        ),
    ]
