from django.db import models
import datetime

DATE_FORMAT = "%Y-%m-%d"

# Create your models here.
class StockScheduleManager(models.Model):
    # defauult value is current date
    date = models.TextField(blank=False, null=False, unique=True, default=datetime.datetime.now().strftime(DATE_FORMAT))
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ["-created_at"]
