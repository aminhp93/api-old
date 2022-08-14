# users/urls.py
...
from django.urls import include, path

from .views import FireBaseAuthAPI, public, protected

urlpatterns = [
    path('firebase/auth/', FireBaseAuthAPI.as_view(), name='firebase_auth'),
    path('public/', public, name='public'),
    path('protected/', protected, name='protected'),
]
