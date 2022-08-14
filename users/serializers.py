# users/serializers.py

from rest_framework import serializers

class FireBaseAuthSerializer(serializers.Serializer):
    token = serializers.CharField()
