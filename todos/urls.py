from django.urls import path
from .views import (
    CreateTodoAPIView,
    ListTodoAPIView,
    DetailTodoAPIView,
)

app_name = "todos"

urlpatterns = [
    path("", ListTodoAPIView.as_view(), name="list_todo"),
    path("create/", CreateTodoAPIView.as_view(), name="create_todo"),
    path("<int:id>/", DetailTodoAPIView.as_view(), name="todo_detail"),
]