from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class Tag(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
