from django.db import models

# Create your models here.

class Stock(models.Model):

    # key: "HPG_2022-11-28"
    # adjRatio: 1
    # buyCount: 18808
    # buyForeignQuantity: 22667864
    # buyForeignValue: 367095950000
    # buyQuantity: 98277150
    # currentForeignRoom: 1695520523
    # date: "2022-11-28T00:00:00"
    # dealVolume: 58844900
    # priceAverage: 16.11906
    # priceBasic: 15.3
    # priceClose: 16.35
    # priceHigh: 16.35
    # priceLow: 15.6
    # priceOpen: 15.6
    # propTradingNetDealValue: 11145075000
    # propTradingNetPTValue: 0
    # propTradingNetValue: 11145075000
    # putthroughValue: 1151850000
    # putthroughVolume: 77000
    # sellCount: 20335
    # sellForeignQuantity: 3276699
    # sellForeignValue: 52627540000
    # sellQuantity: 78495636
    # symbol: "HPG"
    # totalValue: 949676323794
    # totalVolume: 58921900

    key = models.CharField(unique=True, null=False, blank=False, max_length=30)
    adjRatio = models.FloatField()
    buyCount = models.FloatField()
    buyForeignQuantity = models.FloatField()
    buyForeignValue = models.FloatField()
    buyQuantity = models.FloatField()
    currentForeignRoom = models.FloatField()
    date = models.CharField(max_length=30)
    dealVolume = models.FloatField()
    priceAverage = models.FloatField()
    priceBasic = models.FloatField()
    priceClose = models.FloatField()
    priceHigh = models.FloatField()
    priceLow = models.FloatField()
    priceOpen = models.FloatField()
    propTradingNetDealValue = models.FloatField()
    propTradingNetPTValue = models.FloatField()
    propTradingNetValue = models.FloatField()
    putthroughValue = models.FloatField()
    putthroughVolume = models.FloatField()
    sellCount = models.FloatField()
    sellForeignQuantity = models.FloatField()
    sellForeignValue = models.FloatField()
    sellQuantity = models.FloatField()
    symbol = models.CharField(max_length=10)
    totalValue = models.FloatField()
    totalVolume = models.FloatField()


    def __str__(self):
        return self.key