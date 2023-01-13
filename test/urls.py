from django.urls import path
from .views import (
    TestList,
    TestDetail,
    test_start_job,
    test_cancel_job,
    test
)

app_name = "tests"

urlpatterns = [
    path('', TestList.as_view()),
    path('test/', test),
    path('start-job/', test_start_job),
    path('cancel-job/', test_cancel_job),
    path('<int:pk>/', TestDetail.as_view()),
    
]