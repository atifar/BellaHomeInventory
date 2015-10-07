from django.db import models

from inventory.models import Category, Subcategory, ProductVariant, Status


class Keyword(models.Model):
    word = models.CharField(max_length=200)

    def __str__(self):
        return self.word


class CsCartProduct(models.Model):
    prod_variant = models.ForeignKey(ProductVariant, null=True,
                                     on_delete=models.SET_NULL)
    list_price = models.FloatField(default=0)
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=1200, blank=True)
    extra_shipping_cost = models.FloatField(default=0)

    def __str__(self):
        if self.prod_variant:
            return self.prod_variant.product.name
        else:
            return 'NULL'


class CsCartCategory(models.Model):
    category = models.OneToOneField(Category)
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=1200, blank=True)
    keyword = models.ManyToManyField(Keyword, blank=True)
    status = models.ForeignKey(Status)

    def __str__(self):
        return self.category.name


class CsCartSubcategory(models.Model):
    subcategory = models.OneToOneField(Subcategory)
    page_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=1200, blank=True)
    keyword = models.ManyToManyField(Keyword, blank=True)
    status = models.ForeignKey(Status)

    def __str__(self):
        return self.subcategory.name
