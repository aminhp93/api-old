import os
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Todo

User = get_user_model()


class TodoCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'body'
        ]


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'


class TodoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'
