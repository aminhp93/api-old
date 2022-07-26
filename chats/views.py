from django.shortcuts import render
import pusher
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework import status

from .models import Chat
from .serializers import ChatSerializer
from .paginations import ChatLimitOffsetPagination

# Create your views here.

class ChatList(APIView):
    """
    List all chats, or create a new chat.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ChatLimitOffsetPagination

    def get(self, request, *args, **kwargs):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(sender=request.user)
            
            PUSHER_CONFIG = {
                'app_id': '1435319',
                'key': '15ee77871e1ed5258044',
                'secret': '4c2b97bec11d18dc8a13',
                'cluster': 'ap1',
            }
            
            pusher_client = pusher.Pusher(
                app_id=PUSHER_CONFIG['app_id'],
                key=PUSHER_CONFIG['key'],
                secret=PUSHER_CONFIG['secret'],
                cluster=PUSHER_CONFIG['cluster']
                )

            pusher_client.trigger('chat', 'message', serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatDetail(APIView):
    """
    Retrieve, update or delete a chat instance.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Chat.objects.get(pk=pk)
        except Chat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        chat = self.get_object(pk)
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        chat = self.get_object(pk)
        serializer = ChatSerializer(chat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        chat = self.get_object(pk)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    