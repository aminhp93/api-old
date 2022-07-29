from django.urls import path
from .views import (
    ChatList,
    ChatDetail,
    ChatViewSet,
    PuhserAuthenticationAPI
)

app_name = "chats"

urlpatterns = [
    path('', ChatList.as_view()),
    path('<int:pk>/', ChatDetail.as_view()),
    path('pusher/auth/', PuhserAuthenticationAPI.as_view({ 'post': 'pusher_authentication'})),
    # path('', ChatViewSet.as_view({'get': 'list'})),
    # path('<int:pk>/', ChatViewSet.as_view({'get': 'retrieve'})),

]