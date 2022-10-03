from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Todo(models.Model):
    title = models.CharField(blank=True, max_length=100, null=True)
    body = models.TextField(blank=True, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    is_done = models.BooleanField(default=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.id
    class Meta:
        ordering = ["-created_at", "-updated_at"]
