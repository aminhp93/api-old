from django.urls import path
from .views import (
    CreateProblemAPIView,
    ListProblemAPIView,
    DetailProblemAPIView,
)

app_name = "problems"

urlpatterns = [
    path("", ListProblemAPIView.as_view(), name="list_problem"),
    path("create/", CreateProblemAPIView.as_view(), name="create_problem"),
    path("<int:id>/", DetailProblemAPIView.as_view(), name="problem_detail"),
]