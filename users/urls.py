# users/urls.py
...
from django.urls import include, path

from .views import FireBaseAuthAPI, public, protected

app_name = 'users'

urlpatterns = [
    path('firebase/auth/', FireBaseAuthAPI.as_view()),
    path('public/', public),
    path('protected/', protected),
]
