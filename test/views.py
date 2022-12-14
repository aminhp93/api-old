from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Test
from .serializers import TestSerializer
from rest_framework import status
import schedule
import time
from rest_framework.decorators import api_view, permission_classes
from datetime import datetime, timezone, timedelta
from dateutil import tz
import pytz
from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification


DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class TestList(APIView):
    
    """
    List all tests, or create a new test.
    """
    def get(self, request, format=None):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TestDetail(APIView):
    """
    Retrieve, update or delete a test instance.
    """
    def get_object(self, pk):
        try:
            return Test.objects.get(pk=pk)
        except Test.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        test = self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view()
def test_start_job(requet):
    local = pytz.timezone("Asia/Saigon")
    now = datetime.now()
    naive = datetime.strptime("2022-12-12 13:54:00", DATE_FORMAT)
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)


    schedule.every().minute.at(':06').do(task).tag('test-tag-1')
    while True:
        schedule.run_pending()
        time.sleep(1)
    return Response({ "message": "Start job"})

@api_view()
def test_cancel_job(requet):

    print(' cancel job')
    all_jobs = schedule.get_jobs()
    print(all_jobs)
    # schedule.clear()
    return Response({ "message": "Cancel job"})

def task():
    # datetime object containing current date and time
    now = datetime.now()
    device = FCMDevice.objects.all().filter(active=True)
    print(device)
    title = "Test title"
    body = "Test body"
    device.send_message(Message(notification=Notification(title=title, body=body, image="image_url")))
    print("I'm working...", now.strftime(DATE_FORMAT))



