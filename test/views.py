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
import requests
import json

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
    naive = datetime.strptime("2023-01-13 15:23:00", DATE_FORMAT)
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)


    # schedule.every().minute.at(':06').do(task).tag('test-tag-1')
    print(now)
    schedule.every().day.at("08:48").do(task_import)

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


@api_view()
async def test(requet):
    # call api 10 times and wait all to get final data
    print('start')
    # data = []
    # for i in ['HPG','HSG','NKG','SHI','SMC','TLH','ABB','ACB','BID','BVB','CTG','HDB','KLB','LPB','MBB','MSB','NAB','NVB','OCB','PGB','SHB','STB','TCB','TPB','VIB','VPB','EIB','SGB','SSB','VBB','VCB','AGG','D2D','DIG','DXG','HDC','HDG','HPX','IJC','KDH','LHG','NLG','NTL','NVL','PDR','SJS','TDC','TIG','TIP','KBC','SCR','KHG','CRE','HQC','CKG','AGR','BSI','BVS','CTS','FTS','HCM','MBS','ORS','SHS','SSI','TVB','VCI','VIX','VND','VDS','SBS','BSR','OIL','PLX','PVD','PVS','PVC','ADS','DLG','APG','PAS','TCD','DRC','OGC','DDG','AMV','FIT','MST','HAX','DPR','VGS','IPA','MBG','HHS','ITC','BCM','LDG','GEG','LCG','EVG','AAT','KOS','VC3','HVN','TTF','DDV','PTB','PET','DXS','CSV','FIR','NT2','NBB','DPG','SAM','VGI','SSH','MIG','ABS','FCN','CTF','C4G','KSB','IDI','PNJ','TCM','GMD','CTR','SCG','CTD','SZC','DHC','HBC','VPI','VJC','BCG','VPG','HUT','APH','ANV','REE','HNG','VGC','VHC','HHV','PHR','TNG','AAA','CEO','GAS','PVT','HAH','GVR','BVH','BAF','PC1','GIL','ASM','PAN','SBT','DGW','DBC','FRT','TCH','VRE','DPM','FPT','CII','VCG','DCM','POW','IDC','HAG','MWG','GEX','DGC','HT1','BCC']:
    #     print(i)
    #     url = "https://restv2.fireant.vn/symbols/" + i + "/historical-quotes?startDate=2020-04-18&endDate=2023-01-12&offset=0&limit=20"
    #     payload={}
    #     headers = {
    #         'accept': 'application/json, text/plain, */*',
    #         'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSIsImtpZCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSJ9.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4iLCJhdWQiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4vcmVzb3VyY2VzIiwiZXhwIjoxOTEzNjIzMDMyLCJuYmYiOjE2MTM2MjMwMzIsImNsaWVudF9pZCI6ImZpcmVhbnQudHJhZGVzdGF0aW9uIiwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsInJvbGVzIiwiZW1haWwiLCJhY2NvdW50cy1yZWFkIiwiYWNjb3VudHMtd3JpdGUiLCJvcmRlcnMtcmVhZCIsIm9yZGVycy13cml0ZSIsImNvbXBhbmllcy1yZWFkIiwiaW5kaXZpZHVhbHMtcmVhZCIsImZpbmFuY2UtcmVhZCIsInBvc3RzLXdyaXRlIiwicG9zdHMtcmVhZCIsInN5bWJvbHMtcmVhZCIsInVzZXItZGF0YS1yZWFkIiwidXNlci1kYXRhLXdyaXRlIiwidXNlcnMtcmVhZCIsInNlYXJjaCIsImFjYWRlbXktcmVhZCIsImFjYWRlbXktd3JpdGUiLCJibG9nLXJlYWQiLCJpbnZlc3RvcGVkaWEtcmVhZCJdLCJzdWIiOiIxZmI5NjI3Yy1lZDZjLTQwNGUtYjE2NS0xZjgzZTkwM2M1MmQiLCJhdXRoX3RpbWUiOjE2MTM2MjMwMzIsImlkcCI6IkZhY2Vib29rIiwibmFtZSI6Im1pbmhwbi5vcmcuZWMxQGdtYWlsLmNvbSIsInNlY3VyaXR5X3N0YW1wIjoiODIzMzcwOGUtYjFjOS00ZmQ3LTkwYmYtMzI2NTYzYmU4N2JkIiwianRpIjoiZmIyZWJkNzAzNTBiMDBjMGJhMWE5ZDA5NGUwNDMxMjYiLCJhbXIiOlsiZXh0ZXJuYWwiXX0.OhgGCRCsL8HVXSueC31wVLUhwWWPkOu-yKTZkt3jhdrK3MMA1yJroj0Y73odY9XSLZ3dA4hUTierF0LxcHgQ-pf3UXR5KYU8E7ieThAXnIPibWR8ESFtB0X3l8XYyWSYZNoqoUiV9NGgvG2yg0tQ7lvjM8UYbiI-3vUfWFsMX7XU3TQnhxW8jYS_bEXEz7Fvd_wQbjmnUhQZuIVJmyO0tFd7TGaVipqDbRdry3iJRDKETIAMNIQx9miHLHGvEqVD5BsadOP4l8M8zgVX_SEZJuYq6zWOtVhlq3uink7VvnbZ7tFahZ4Ty4z8ev5QbUU846OZPQyMlEnu_TpQNpI1hg',
    #     }

    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     data.append(response.json())


    url_1 = "https://restv2.fireant.vn/symbols/HPG/historical-quotes?startDate=2020-04-18&endDate=2023-01-12&offset=0&limit=20"
    payload_1 ={}
    headers_1 = {
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSIsImtpZCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSJ9.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4iLCJhdWQiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4vcmVzb3VyY2VzIiwiZXhwIjoxOTEzNjIzMDMyLCJuYmYiOjE2MTM2MjMwMzIsImNsaWVudF9pZCI6ImZpcmVhbnQudHJhZGVzdGF0aW9uIiwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsInJvbGVzIiwiZW1haWwiLCJhY2NvdW50cy1yZWFkIiwiYWNjb3VudHMtd3JpdGUiLCJvcmRlcnMtcmVhZCIsIm9yZGVycy13cml0ZSIsImNvbXBhbmllcy1yZWFkIiwiaW5kaXZpZHVhbHMtcmVhZCIsImZpbmFuY2UtcmVhZCIsInBvc3RzLXdyaXRlIiwicG9zdHMtcmVhZCIsInN5bWJvbHMtcmVhZCIsInVzZXItZGF0YS1yZWFkIiwidXNlci1kYXRhLXdyaXRlIiwidXNlcnMtcmVhZCIsInNlYXJjaCIsImFjYWRlbXktcmVhZCIsImFjYWRlbXktd3JpdGUiLCJibG9nLXJlYWQiLCJpbnZlc3RvcGVkaWEtcmVhZCJdLCJzdWIiOiIxZmI5NjI3Yy1lZDZjLTQwNGUtYjE2NS0xZjgzZTkwM2M1MmQiLCJhdXRoX3RpbWUiOjE2MTM2MjMwMzIsImlkcCI6IkZhY2Vib29rIiwibmFtZSI6Im1pbmhwbi5vcmcuZWMxQGdtYWlsLmNvbSIsInNlY3VyaXR5X3N0YW1wIjoiODIzMzcwOGUtYjFjOS00ZmQ3LTkwYmYtMzI2NTYzYmU4N2JkIiwianRpIjoiZmIyZWJkNzAzNTBiMDBjMGJhMWE5ZDA5NGUwNDMxMjYiLCJhbXIiOlsiZXh0ZXJuYWwiXX0.OhgGCRCsL8HVXSueC31wVLUhwWWPkOu-yKTZkt3jhdrK3MMA1yJroj0Y73odY9XSLZ3dA4hUTierF0LxcHgQ-pf3UXR5KYU8E7ieThAXnIPibWR8ESFtB0X3l8XYyWSYZNoqoUiV9NGgvG2yg0tQ7lvjM8UYbiI-3vUfWFsMX7XU3TQnhxW8jYS_bEXEz7Fvd_wQbjmnUhQZuIVJmyO0tFd7TGaVipqDbRdry3iJRDKETIAMNIQx9miHLHGvEqVD5BsadOP4l8M8zgVX_SEZJuYq6zWOtVhlq3uink7VvnbZ7tFahZ4Ty4z8ev5QbUU846OZPQyMlEnu_TpQNpI1hg',
    }

    response_1 = requests.request("GET", url_1, headers=headers_1, data=payload_1)

    url = "https://bnimawsouehpkbipqqvl.supabase.co/rest/v1/stock_test?select=id"

    data_payload = response_1.json()[0]

    data_payload['key'] = data_payload['symbol'] + "_" + data_payload['date']
    print(data_payload)
    payload = json.dumps(data_payload)

    # payload = json.dumps({
    #     "adjRatio": 1,
    #     "buyCount": 10675,
    #     "buyForeignQuantity": 4823710,
    #     "buyForeignValue": 97158460000,
    #     "buyQuantity": 36232974,
    #     "currentForeignRoom": 1551815420,
    #     "date": "2023-01-12T00:00:00",
    #     "dealVolume": 20172900,
    #     "priceAverage": 20.11849,
    #     "priceBasic": 20.2,
    #     "priceClose": 20.05,
    #     "priceHigh": 20.25,
    #     "priceLow": 19.9,
    #     "priceOpen": 20.1,
    #     "propTradingNetDealValue": -1386460000,
    #     "propTradingNetPTValue": 0,
    #     "propTradingNetValue": -1386460000,
    #     "putthroughValue": 58202000000,
    #     "putthroughVolume": 3024000,
    #     "sellCount": 9802,
    #     "sellForeignQuantity": 784610,
    #     "sellForeignValue": 15784960000,
    #     "sellQuantity": 43870440,
    #     "symbol": "HPG",
    #     "totalValue": 464050286921,
    #     "totalVolume": 23196900,
    #     "key": "HPG_2023-01-12T00:00:00"
    # })
    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJuaW1hd3NvdWVocGtiaXBxcXZsIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzM0NDY4MzcsImV4cCI6MTk4OTAyMjgzN30.K_BGIC_TlWbHl07XX94EWxRI_2Om_NKu_PY5pGtG-hk',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJuaW1hd3NvdWVocGtiaXBxcXZsIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzM0NDY4MzcsImV4cCI6MTk4OTAyMjgzN30.K_BGIC_TlWbHl07XX94EWxRI_2Om_NKu_PY5pGtG-hk',
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    
    print('done')
    return Response({ "message": response.text })

def task_import():

    data = []
    for i in ['HPG','HSG','NKG','SHI','SMC','TLH','ABB','ACB','BID','BVB','CTG','HDB','KLB','LPB','MBB','MSB','NAB','NVB','OCB','PGB','SHB','STB','TCB','TPB','VIB','VPB','EIB','SGB','SSB','VBB','VCB','AGG','D2D','DIG','DXG','HDC','HDG','HPX','IJC','KDH','LHG','NLG','NTL','NVL','PDR','SJS','TDC','TIG','TIP','KBC','SCR','KHG','CRE','HQC','CKG','AGR','BSI','BVS','CTS','FTS','HCM','MBS','ORS','SHS','SSI','TVB','VCI','VIX','VND','VDS','SBS','BSR','OIL','PLX','PVD','PVS','PVC','ADS','DLG','APG','PAS','TCD','DRC','OGC','DDG','AMV','FIT','MST','HAX','DPR','VGS','IPA','MBG','HHS','ITC','BCM','LDG','GEG','LCG','EVG','AAT','KOS','VC3','HVN','TTF','DDV','PTB','PET','DXS','CSV','FIR','NT2','NBB','DPG','SAM','VGI','SSH','MIG','ABS','FCN','CTF','C4G','KSB','IDI','PNJ','TCM','GMD','CTR','SCG','CTD','SZC','DHC','HBC','VPI','VJC','BCG','VPG','HUT','APH','ANV','REE','HNG','VGC','VHC','HHV','PHR','TNG','AAA','CEO','GAS','PVT','HAH','GVR','BVH','BAF','PC1','GIL','ASM','PAN','SBT','DGW','DBC','FRT','TCH','VRE','DPM','FPT','CII','VCG','DCM','POW','IDC','HAG','MWG','GEX','DGC','HT1','BCC']:
        print(i)
        url_1 = "https://restv2.fireant.vn/symbols/" + i + "/historical-quotes?startDate=2020-04-18&endDate=2023-01-12&offset=0&limit=20"
        
        headers_1 = {
            'accept': 'application/json, text/plain, */*',
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSIsImtpZCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSJ9.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4iLCJhdWQiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4vcmVzb3VyY2VzIiwiZXhwIjoxOTEzNjIzMDMyLCJuYmYiOjE2MTM2MjMwMzIsImNsaWVudF9pZCI6ImZpcmVhbnQudHJhZGVzdGF0aW9uIiwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsInJvbGVzIiwiZW1haWwiLCJhY2NvdW50cy1yZWFkIiwiYWNjb3VudHMtd3JpdGUiLCJvcmRlcnMtcmVhZCIsIm9yZGVycy13cml0ZSIsImNvbXBhbmllcy1yZWFkIiwiaW5kaXZpZHVhbHMtcmVhZCIsImZpbmFuY2UtcmVhZCIsInBvc3RzLXdyaXRlIiwicG9zdHMtcmVhZCIsInN5bWJvbHMtcmVhZCIsInVzZXItZGF0YS1yZWFkIiwidXNlci1kYXRhLXdyaXRlIiwidXNlcnMtcmVhZCIsInNlYXJjaCIsImFjYWRlbXktcmVhZCIsImFjYWRlbXktd3JpdGUiLCJibG9nLXJlYWQiLCJpbnZlc3RvcGVkaWEtcmVhZCJdLCJzdWIiOiIxZmI5NjI3Yy1lZDZjLTQwNGUtYjE2NS0xZjgzZTkwM2M1MmQiLCJhdXRoX3RpbWUiOjE2MTM2MjMwMzIsImlkcCI6IkZhY2Vib29rIiwibmFtZSI6Im1pbmhwbi5vcmcuZWMxQGdtYWlsLmNvbSIsInNlY3VyaXR5X3N0YW1wIjoiODIzMzcwOGUtYjFjOS00ZmQ3LTkwYmYtMzI2NTYzYmU4N2JkIiwianRpIjoiZmIyZWJkNzAzNTBiMDBjMGJhMWE5ZDA5NGUwNDMxMjYiLCJhbXIiOlsiZXh0ZXJuYWwiXX0.OhgGCRCsL8HVXSueC31wVLUhwWWPkOu-yKTZkt3jhdrK3MMA1yJroj0Y73odY9XSLZ3dA4hUTierF0LxcHgQ-pf3UXR5KYU8E7ieThAXnIPibWR8ESFtB0X3l8XYyWSYZNoqoUiV9NGgvG2yg0tQ7lvjM8UYbiI-3vUfWFsMX7XU3TQnhxW8jYS_bEXEz7Fvd_wQbjmnUhQZuIVJmyO0tFd7TGaVipqDbRdry3iJRDKETIAMNIQx9miHLHGvEqVD5BsadOP4l8M8zgVX_SEZJuYq6zWOtVhlq3uink7VvnbZ7tFahZ4Ty4z8ev5QbUU846OZPQyMlEnu_TpQNpI1hg',
        }

        response_1 = requests.request("GET", url_1, headers=headers_1)
        data_payload = response_1.json()[0]
        data_payload['key'] = data_payload['symbol'] + "_" + data_payload['date']
        data.append(data_payload)

    
    url = "https://bnimawsouehpkbipqqvl.supabase.co/rest/v1/stock_test?select=id"

    payload = json.dumps(data)

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJuaW1hd3NvdWVocGtiaXBxcXZsIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzM0NDY4MzcsImV4cCI6MTk4OTAyMjgzN30.K_BGIC_TlWbHl07XX94EWxRI_2Om_NKu_PY5pGtG-hk',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJuaW1hd3NvdWVocGtiaXBxcXZsIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzM0NDY4MzcsImV4cCI6MTk4OTAyMjgzN30.K_BGIC_TlWbHl07XX94EWxRI_2Om_NKu_PY5pGtG-hk',
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
    }

    requests.request("POST", url, headers=headers, data=payload)

    print('DONE')


