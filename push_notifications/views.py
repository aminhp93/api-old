from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice
# Create your views here.

class PushNotificationTest(GenericAPIView):

    def post(self, request, *args, **kwargs):
        # Get device id
        device = FCMDevice.objects.all().first()
        device.send_message(Message(notification=Notification(title="title", body="body", image="image_url")))
        return Response({ "PushNotificationTest": "ok"})