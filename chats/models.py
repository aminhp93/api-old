from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Chat(models.Model):
    message = models.TextField(blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
