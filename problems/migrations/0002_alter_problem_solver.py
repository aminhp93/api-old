# Generated by Django 4.0.6 on 2022-10-07 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='solver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solver_problem', to=settings.AUTH_USER_MODEL),
        ),
    ]
