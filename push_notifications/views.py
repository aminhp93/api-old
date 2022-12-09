from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice
# Create your views here.

class PushNotificationTest(GenericAPIView):

    def post(self, request, *args, **kwargs):
        # Get device id
        title = request.data.get('title')
        if not title:
            title = "No title"
        
        body = request.data.get('body')
        if not body:
            body = "No body"

        device = FCMDevice.objects.all().filter(active=True)
        print(device)
        device.send_message(Message(notification=Notification(title=title, body=body, image="image_url")))
        return Response({ "PushNotificationTest": "ok"})

class PushNotificationCreateTokenView(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    def post(self, request, *args, **kwargs):
        token = request.data.get("token")
        device = FCMDevice.objects.filter(registration_id=token).first()
        if device:
           return Response({ "message": "Token regsitered"})

        fcm_device = FCMDevice()
        fcm_device.registration_id = token
        fcm_device.user = request.user
        fcm_device.save()
        return Response({ "message": "Create new token success"})
