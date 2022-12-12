from django.urls import path
from .views import (
    TagsApiView,
)

app_name = "tags"

urlpatterns = [
    path('', TagsApiView.as_view()),
]