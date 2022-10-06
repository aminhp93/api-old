# users/urls.py
...
from django.urls import include, path

from .views import PaymentMomoTest

app_name = 'payments'

urlpatterns = [
    path('', PaymentMomoTest.as_view()),
    
]
