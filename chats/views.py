from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView
)
# Create your views here.
import pusher



class ListChatAPIView(ListAPIView):

    def get(self, request):
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

        pusher_client.trigger('chat', 'message', {u'message': u'hello world'})
        return Response({1: 'a'})