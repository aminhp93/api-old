from rest_framework import serializers
from .models import Tag

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'id')
