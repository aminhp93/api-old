# Generated by Django 4.0.6 on 2022-12-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_alter_stock_buycount_alter_stock_buyforeignquantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='adjRatio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='buyCount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='buyForeignQuantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='buyForeignValue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='buyQuantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='currentForeignRoom',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='dealVolume',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='priceAverage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='priceBasic',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='priceClose',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='priceHigh',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='priceLow',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='priceOpen',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='propTradingNetDealValue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='propTradingNetPTValue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='propTradingNetValue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='putthroughValue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='putthroughVolume',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sellCount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sellForeignQuantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sellForeignValue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sellQuantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='totalValue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='totalVolume',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
