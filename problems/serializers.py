import os
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Problem

User = get_user_model()


class ProblemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = [
            'problem_src'
        ]


class ProblemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = '__all__'


class ProblemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = '__all__'
