from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from auth.permissions import TestPermission

from .paginations import PostLimitOffsetPagination
from .models import Post, Comment
from .permissions import IsOwnerOrReadOnly, IsOwner
from .mixins import MultipleFieldLookupMixin
from .serializers import (
    PostCreateUpdateSerializer,
    PostListSerializer,
    PostDetailSerializer,
    CommentSerializer,
    CommentCreateUpdateSerializer,
)

# Create your views here.
class CreatePostAPIView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = PostCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class ListPostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PostLimitOffsetPagination


class DetailPostAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = "id"
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CreateCommentAPIView(APIView):

    serializer_class = CommentCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return Response({ data: "Hello World" }, status=200)
        # post = get_object_or_404(Post, id=id)
        # serializer = CommentCreateUpdateSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save(author=request.user, parent=post)
        #     return Response(serializer.data, status=200)
        # else:
        #     return Response({"errors": serializer.errors}, status=400)


class ListCommentAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({ data: "Hello World" }, status=200)
        # post = Post.objects.get(id=id)
        # comments = Comment.objects.filter(parent=post)
        # serializer = CommentSerializer(comments, many=True)
        # return Response(serializer.data, status=200)


# class DetailCommentAPIView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     queryset = Comment.objects.all()
#     lookup_fields = ["parent", "id"]
#     serializer_class = CommentCreateUpdateSerializer