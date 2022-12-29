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

from .models import Stock
from .serializers import (
   StockSerializer,
   StockListSerializer
)
from rest_framework.parsers import JSONParser


# Create your views here.
class CreateStockAPIView(APIView):
    """
    post:
        Creates a new todo instance. Returns created todo data

        parameters: [body]
    """

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = []
    parser_classes = [JSONParser]


    def post(self, request, *args, **kwargs):
        # delete all data in table 
        # print(request.data)
        
        # Stock.objects.all().delete()
        
        # create array with 100000 item to data
        data = request.data
        # data = []
        
        # for i in range(1):
        #     data.append({
        #         "key": "HPG_2022-11-" + str(i),
        #         "adjRatio": 1,
        #         "buyCount": 18808,
        #         "buyForeignQuantity": 22667864,
        #         "buyForeignValue": 367095950000,
        #         "buyQuantity": 98277150,
        #         "currentForeignRoom": 1695520523,
        #         "date": "2022-11-28",
        #         "dealVolume": 58844900,
        #         "priceAverage": 16.11906,
        #         "priceBasic": 15.3,
        #         "priceClose": 16.35,
        #         "priceHigh": 16.35,
        #         "priceLow": 15.6,
        #         "priceOpen": 15.6,
        #         "propTradingNetDealValue": 11145075000,
        #         "propTradingNetPTValue": 0,
        #         "propTradingNetValue": 11145075000,
        #         "putthroughValue": 1151850000,
        #         "putthroughVolume": 77000,
        #         "sellCount": 20335,
        #         "sellForeignQuantity": 3276699,
        #         "sellForeignValue": 52627540000,
        #         "sellQuantity": 78495636,
        #         "symbol": "HPG",
        #         "totalValue": 949676323794,
        #         "totalVolume": 58921900,
        #     })
        # print(data)

        serializer = StockSerializer(data=data, many=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)

class DeleteStockAPIView(APIView):
    def post(self, request, *args, **kwargs):
        Stock.objects.all().delete()
        return Response({"message": "Delete all data"}, status=200)


class ListStockAPIView(ListAPIView):
    """
    get:
        Returns a list of all existing posts
    """

    serializer_class = StockListSerializer
    permission_classes = []
    pagination_class = None

    def get_queryset(self):
        symbols = self.request.query_params.get('symbols', None)
        if symbols:
            symbols = symbols.split(",")
            print(symbols)
            return Stock.objects.filter(symbol__in=symbols)
        return Stock.objects.all()