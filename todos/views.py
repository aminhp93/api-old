from django.shortcuts import render
import json
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

from .paginations import TodoLimitOffsetPagination
from .models import Todo
from .permissions import IsOwnerOrReadOnly, IsOwner
from .serializers import (
    TodoCreateUpdateSerializer,
    TodoListSerializer,
    TodoDetailSerializer,
)


# Create your views here.
class CreateTodoAPIView(APIView):
    """
    post:
        Creates a new todo instance. Returns created todo data

        parameters: [body]
    """

    queryset = Todo.objects.all()
    serializer_class = TodoCreateUpdateSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        # Check if user has less than 5 active todos
        if Todo.objects.filter(author=request.user, is_done=False).count() >= 5:
            return Response(
                {"error": "You can only have 5 active todos at a time"},
                status=400,
            )            

        serializer = TodoCreateUpdateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class ListTodoAPIView(ListAPIView):
    """
    get:
        Returns a list of all existing posts
    """

    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TodoLimitOffsetPagination

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        params_id_done = self.request.query_params.get("is_done", None)
        if params_id_done is not None:
            is_done = json.loads(params_id_done)
            if is_done is not None:
                return Todo.objects.filter(author=self.request.user, is_done=is_done)
        return Todo.objects.all()


class DetailTodoAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a todo instance. Searches todo using id field.

    put:
        Updates an existing todo. Returns updated todo data

        parameters: [id, title, body, description, image]

    delete:
        Delete an existing todo

        parameters = [id]
    """

    queryset = Todo.objects.all()
    lookup_field = "id"
    serializer_class = TodoDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


