from django.urls import path
from .views import (
    CreateStockAPIView,
    ListStockAPIView,
    DeleteStockAPIView,
    list_stock_jobs,
    start_daily_import_stock_job,
    cancel_daily_import_stock_job,
    force_daily_import_stock_job
)

app_name = "stocks"

urlpatterns = [
    path("", ListStockAPIView.as_view(), name="list_stock"),
    path("create/", CreateStockAPIView.as_view(), name="create_stock"),
    path("delete/", DeleteStockAPIView.as_view(), name="delete_stock"),
    path("list-stock-jobs/", list_stock_jobs, name="list_stock_jobs"),
    path("start-daily-import-stock-job/", start_daily_import_stock_job, name="start_daily_import_stock_job"),
    path("cancel-daily-import-stock-job/", cancel_daily_import_stock_job, name="cancel_daily_import_stock_job"),
    path("force-daily-import-stock-job/", force_daily_import_stock_job, name="force_daily_import_stock_job"),
]
