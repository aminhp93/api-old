# Generated by Django 4.0.6 on 2022-10-01 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='slug',
        ),
    ]
