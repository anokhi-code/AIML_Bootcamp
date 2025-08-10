from django.db import models
class Product (models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.CharField(max_length=30)
    product_quantity = models.CharField(max_length=30)

# Create your models here.
