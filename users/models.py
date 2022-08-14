from tabnanny import verbose
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        null=True,
        blank=True
    )
    firebase_user_id = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self: "CustomUser") -> str:
        return f"{self.email}"