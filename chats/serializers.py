from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
