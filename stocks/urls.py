from django.urls import path
from .views import (
    CreateStockAPIView,
    ListStockAPIView,
)

app_name = "stocks"

urlpatterns = [
    path("", ListStockAPIView.as_view(), name="list_stock"),
    path("create/", CreateStockAPIView.as_view(), name="create_stock"),
]
