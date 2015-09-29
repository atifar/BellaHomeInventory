from django.db import models


class Image(models.Model):
    image_file = models.ImageField()
    thumbnail_file = models.ImageField()


class Category(models.Model):
    image = models.ManyToManyField(Image)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    keyword_list = models.TextField(max_length=1500, blank=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    image = models.ManyToManyField(Image)
    category_id = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    keyword_list = models.TextField(max_length=1500, blank=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    color = models.CharField(max_length=100, blank=True)


class Size(models.Model):
    size_code = models.CharField(max_length=100, blank=True)
    width = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=100, blank=True)
    depth = models.CharField(max_length=100, blank=True)


class Status(models.Model):
    status = models.CharField(max_length=100)


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    phone = models.IntegerField()
    fax = models.IntegerField()
    email = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    short_description = models.TextField(max_length=250, blank=True)
    special_order = models.BooleanField(default=False)


class ProductVariant(models.Model):
    supplier_id = models.ForeignKey(Supplier)
    product_id = models.ForeignKey(Product)
    color_id = models.ForeignKey(Color)
    size_id = models.ForeignKey(Size)
    status_id = models.ForeignKey(Status)
    image = models.ManyToManyField(Image)
    upc = models.IntegerField()
    weight = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    msrp = models.FloatField()


class Inventory(models.Model):
    product_id = models.ForeignKey(ProductVariant)
    quantity_on_hand = models.IntegerField()


