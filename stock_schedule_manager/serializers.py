from rest_framework import serializers

from .models import StockScheduleManager

class StockScheduleManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockScheduleManager
        fields = '__all__'
