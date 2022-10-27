from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    barcode = models.CharField(max_length=100)
    reseller_id = models.IntegerField()
    img_url = models.CharField(max_length=2083)