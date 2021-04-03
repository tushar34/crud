from django.db import models

# Create your models here.
class Cardata(models.Model):
    objects = None
    c_company = models.CharField(max_length=20)
    c_name = models.CharField(max_length=20)
    c_price = models.CharField(max_length=20)
