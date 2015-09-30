from django.db import models

from inventory.models import Category, Subcategory, ProductVariant


class CsCartProduct(models.Model):
    prod_variant_id = models.ForeignKey(ProductVariant)
    list_price = models.FloatField()
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    keyword_list = models.CharField(max_length=500)
    extra_shipping_cost = models.FloatField()

    def __str__(self):
        return self.id


class CsCartCategory(models.Model):
    category_id = models.OneToOneField(Category)
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    keyword_list = models.CharField(max_length=500)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class CsCartSubcategory(models.Model):
    subcategory_id = models.OneToOneField(Subcategory)
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    keyword_list = models.CharField(max_length=500)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.id

