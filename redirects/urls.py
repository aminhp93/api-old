from django.urls import path
from .views import (
    RedirectView
)

app_name = "redirects"

urlpatterns = [
    path('', RedirectView.as_view())
]