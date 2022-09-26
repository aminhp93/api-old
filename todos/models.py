from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse

User = get_user_model()

# Create your models here.
class Todo(models.Model):
    slug = models.SlugField()
    title = models.CharField(blank=True, max_length=100, null=True)
    body = models.TextField(blank=True, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    is_done = models.BooleanField(default=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    def get_api_url(self):
        try:
            return reverse("todos_api:todo_detail", kwargs={"slug": self.slug})
        except Exception:
            None

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Todo.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_todo_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_todo_receiver, sender=Todo)
