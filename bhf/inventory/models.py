from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    short_description = models.TextField(max_length=250, blank=True)
    special_order = models.BooleanField()
