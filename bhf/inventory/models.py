from django.db import models


class Image(models.Model):
    image_file = models.ImageField(blank=True)
    thumbnail_file = models.ImageField(blank=True)

    def __str__(self):
        return str(self.id)


class Keyword(models.Model):
    word = models.CharField(max_length=200)

    def __str__(self):
        return self.word


class Category(models.Model):
    image = models.ManyToManyField(Image)
    keyword_id = models.ManyToManyField(Keyword)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1200)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    image = models.ManyToManyField(Image)
    category_id = models.ForeignKey(Category)
    keyword_id = models.ManyToManyField(Keyword)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1200)

    def __str__(self):
        return self.name


class Color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color


class Size(models.Model):
    size_code = models.CharField(max_length=100, blank=True)
    width = models.CharField(max_length=100, blank=True)
    length = models.CharField(max_length=100, blank=True)
    depth = models.CharField(max_length=100, blank=True)

    def __str__(self):
        if not self.size_code:
            return str(self.id)
        else:
            return self.size_code


class Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    phone = models.IntegerField(blank = True)
    fax = models.IntegerField(blank = True)
    email = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    short_description = models.TextField(max_length=250, blank=True)
    special_order = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    subcategory = models.ManyToManyField(Subcategory)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product_id = models.ForeignKey(Product)
    color_id = models.ForeignKey(Color, blank=True, null=True,
                                 on_delete=models.SET_NULL)
    size_id = models.ForeignKey(Size, blank=True, null=True,
                                on_delete=models.SET_NULL)
    status_id = models.ForeignKey(Status)
    supplier_id = models.ManyToManyField(Supplier)
    image = models.ManyToManyField(Image)
    upc = models.IntegerField()
    weight = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=100, blank=True)
    msrp = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)


class Inventory(models.Model):
    product_id = models.OneToOneField(ProductVariant)
    quantity_on_hand = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


