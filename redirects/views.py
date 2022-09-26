from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

# Create your views here.

class Redirect2View(APIView):
    def get(self, request, *args, **kwargs):
        try:
            url = "https://dchart-api.vndirect.com.vn/dchart/search?limit=30&query=FPT&type=&exchange="

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            return Response({'data': response.text})
        except:
            raise Response({'errors': 'Error'})

class RedirectView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            url = request.GET.get('redirect_url')

            if not url:
                return Response({'errors': 'No url'})


            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            return Response(response.json())
        except:
            return Response({'errors': 'Error'})
       
