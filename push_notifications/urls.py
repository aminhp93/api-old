# users/urls.py
...
from django.urls import include, path

from .views import PushNotificationTest

app_name = 'users'

urlpatterns = [
    path('', PushNotificationTest.as_view()),
]
