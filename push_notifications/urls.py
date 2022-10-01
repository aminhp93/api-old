# users/urls.py
...
from django.urls import include, path

from .views import PushNotificationTest, PushNotificationCreateTokenView

app_name = 'users'

urlpatterns = [
    path('', PushNotificationTest.as_view()),
    path('create/', PushNotificationCreateTokenView.as_view()),
    
]
