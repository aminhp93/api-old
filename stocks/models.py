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
    adjRatio = models.FloatField(null=True, blank=True)
    buyCount = models.FloatField(null=True, blank=True)
    buyForeignQuantity = models.FloatField(null=True, blank=True)
    buyForeignValue = models.FloatField(null=True, blank=True)
    buyQuantity = models.FloatField(null=True, blank=True)
    currentForeignRoom = models.FloatField(null=True, blank=True)
    date = models.CharField(max_length=30)
    dealVolume = models.FloatField(null=True, blank=True)
    priceAverage = models.FloatField(null=True, blank=True)
    priceBasic = models.FloatField(null=True, blank=True)
    priceClose = models.FloatField(null=True, blank=True)
    priceHigh = models.FloatField(null=True, blank=True)
    priceLow = models.FloatField(null=True, blank=True)
    priceOpen = models.FloatField(null=True, blank=True)
    propTradingNetDealValue = models.FloatField(null=True, blank=True)
    propTradingNetPTValue = models.FloatField(null=True, blank=True)
    propTradingNetValue = models.FloatField(null=True, blank=True)
    putthroughValue = models.FloatField(null=True, blank=True)
    putthroughVolume = models.FloatField(null=True, blank=True)
    sellCount = models.FloatField(null=True, blank=True)
    sellForeignQuantity = models.FloatField(null=True, blank=True)
    sellForeignValue = models.FloatField(null=True, blank=True)
    sellQuantity = models.FloatField(null=True, blank=True)
    symbol = models.CharField(max_length=10)
    totalValue = models.FloatField(null=True, blank=True)
    totalVolume = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.key