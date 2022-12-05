from django.urls import path
from .views import (
    CreatePostAPIView,
    ListPostAPIView,
    DetailPostAPIView,
    CreateCommentAPIView,
    ListCommentAPIView,
    # DetailCommentAPIView,
)

app_name = "posts"

urlpatterns = [
    path("", ListPostAPIView.as_view(), name="list_post"),
    path("create/", CreatePostAPIView.as_view(), name="create_post"),
    path("<int:id>/", DetailPostAPIView.as_view(), name="post_detail"),
    path("<int:id>/comment/", ListCommentAPIView.as_view(), name="list_comment"),
    path(
        "<int:id>/comment/create/",
        CreateCommentAPIView.as_view(),
        name="create_comment",
    ),
    # path(
    #     "<int:id>/comment/<int:id>/",
    #     DetailCommentAPIView.as_view(),
    #     name="comment_detail",
    # ),
]