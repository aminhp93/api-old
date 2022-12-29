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

class StockListSerializer(serializers.ModelSerializer):
    d = serializers.SerializerMethodField()
    v = serializers.SerializerMethodField()
    c = serializers.SerializerMethodField()
    h = serializers.SerializerMethodField()
    l = serializers.SerializerMethodField()
    o = serializers.SerializerMethodField()
    v2 = serializers.SerializerMethodField()
    s = serializers.SerializerMethodField()

    def get_d(self, obj):
        return obj.date

    def get_v(self, obj):
        return obj.dealVolume

    def get_c(self, obj):
        return obj.priceClose

    def get_h(self, obj):
        return obj.priceHigh

    def get_l(self, obj):
        return obj.priceLow

    def get_o(self, obj):
        return obj.priceOpen

    def get_v2(self, obj):
        return obj.totalVolume

    def get_s(self, obj):
        return obj.symbol
    
    class Meta:
        model = Stock
        fields = [
            'd', # date
            'v', # dealVolume
            'c', # priceClose
            'h', # priceHigh
            'l', # priceLow
            'o', # priceOpen
            'v2', # totalVolume
            's', # symbol
        ]
        # fields = "__all__"