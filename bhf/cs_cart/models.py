from django.db import models

from inventory.models import Category, Subcategory, ProductVariant


class CsCartProduct(models.Model):
    prod_variant_id = models.ForeignKey(ProductVariant)
    list_price = models.FloatField()
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    keyword_list = models.CharField(max_length=500)
    extra_shipping_cost = models.FloatField()


class CsCartCategory(models.Model):
    category_id = models.ForeignKey(Category)
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    keyword_list = models.CharField(max_length=500)
    status = models.CharField(max_length=100)


class CsCartSubcategory(models.Model):
    category_id = models.ForeignKey(Subcategory)
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    keyword_list = models.CharField(max_length=500)
    status = models.CharField(max_length=100)

