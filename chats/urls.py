from django.urls import path
from .views import (
    ListChatAPIView
)

app_name = "chats"

urlpatterns = [
    path("", ListChatAPIView.as_view(), name="list_chat")
]