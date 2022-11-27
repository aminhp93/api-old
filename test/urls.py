from django.urls import path
from .views import (
    TestList,
    TestDetail,
)

app_name = "tests"

urlpatterns = [
    path('', TestList.as_view()),
    path('<int:pk>/', TestDetail.as_view()),
]