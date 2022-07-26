from django.urls import path
from .views import (
    ChatList,
    ChatDetail
)

app_name = "chats"

urlpatterns = [
    path('', ChatList.as_view()),
    path('<int:pk>/', ChatDetail.as_view()),
]