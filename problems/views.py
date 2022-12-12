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

from .paginations import ProblemLimitOffsetPagination
from .models import Problem
from .permissions import IsOwnerOrReadOnly, IsOwner
from .serializers import (
    ProblemCreateUpdateSerializer,
    ProblemListSerializer,
    ProblemDetailSerializer,
)


# Create your views here.
class CreateProblemAPIView(APIView):
    """
    post:
        Creates a new Problem instance. Returns created Problem data

        parameters: [body]
    """

    queryset = Problem.objects.all()
    serializer_class = ProblemCreateUpdateSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = ProblemCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class ListProblemAPIView(ListAPIView):
    """
    get:
        Returns a list of all existing posts
    """

    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ProblemLimitOffsetPagination

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        params_id_done = self.request.query_params.get("isDone", None)
        if params_id_done is not None:
            is_done = json.loads(params_id_done)
            if is_done is not None:
                return Problem.objects.filter(author=self.request.user, is_done=isDone)
        return Problem.objects.all()


class DetailProblemAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a Problem instance. Searches Problem using id field.

    put:
        Updates an existing Problem. Returns updated Problem data

        parameters: [id, title, body, description, image]

    delete:
        Delete an existing Problem

        parameters = [id]
    """

    queryset = Problem.objects.all()
    lookup_field = "id"
    serializer_class = ProblemDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


