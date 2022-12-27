from rest_framework import serializers
from django.db import IntegrityError
from .models import Stock
from rest_framework.exceptions import ValidationError

class BulkCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        return result

class StockSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        instance = Stock(**validated_data)

        if isinstance(self._kwargs["data"], dict):
            instance.save()

        return instance
    
    class Meta:
        model = Stock
        fields = "__all__"
        list_serializer_class = BulkCreateListSerializer