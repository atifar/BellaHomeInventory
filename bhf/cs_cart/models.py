from django.db import models

from inventory.models import Category, Subcategory, ProductVariant


class CsCartProduct(models.Model):
    prod_variant_id = models.ForeignKey(ProductVariant, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    list_price = models.FloatField(default=0)
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=1200, blank=True)
    keyword_list = models.CharField(max_length=1500, blank=True)
    extra_shipping_cost = models.FloatField(default=0)

    def __str__(self):
        return self.id


class CsCartCategory(models.Model):
    category_id = models.OneToOneField(Category)
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=1200, blank=True)
    keyword_list = models.CharField(max_length=1500, blank=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class CsCartSubcategory(models.Model):
    subcategory_id = models.OneToOneField(Subcategory)
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=1200, blank=True)
    keyword_list = models.CharField(max_length=1500, blank=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.id
