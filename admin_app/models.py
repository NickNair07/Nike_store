from django.db import models


# Create your models here.
class CategoryDB(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="category_images")
    description = models.CharField(max_length=255, null=True, blank=True)


class ProductDB(models.Model):
    c_name = models.CharField(max_length=255, null=True, blank=True)
    p_name = models.CharField(max_length=255, null=True, blank=True)
    p_qty = models.IntegerField(null=True, blank=True)
    p_price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    p_image = models.ImageField(upload_to="product_images")
