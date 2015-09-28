from django.db import models

from inventory.models import Image


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    keyword_list = models.TextField(max_length=1500, blank=True)
    image = models.ManyToManyField(Image)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category_id = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    keyword_list = models.TextField(max_length=1500, blank=True)
    image = models.ManyToManyField(Image)

    def __str__(self):
        return self.name


