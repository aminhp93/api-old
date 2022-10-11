from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse

User = get_user_model()

# create random number

# Create your models here.
class Problem(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_problem')
    solver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solver_problem')
    problem_src = models.TextField(blank=False, null=False)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ["-created_at", "-updated_at"]
