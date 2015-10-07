from django.db import models


def upload_handler(instance, filename):
    return 'img/{}'.format(filename)


class Image(models.Model):
    image_file = models.ImageField(upload_to=upload_handler, blank=True)
    thumbnail_file = models.ImageField(upload_to=upload_handler, blank=True)

    def __str__(self):
        return self.image_file.name


class Category(models.Model):
    image = models.ManyToManyField(Image)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1200)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    image = models.ManyToManyField(Image)
    category = models.ForeignKey(Category)
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
            return self.width + ':' + self.length + ':' + self.depth
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
    category = models.ManyToManyField(Category, blank=True)
    subcategory = models.ManyToManyField(Subcategory, blank=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product)
    color = models.ForeignKey(Color, blank=True, null=True,
                                 on_delete=models.SET_NULL)
    size = models.ForeignKey(Size, blank=True, null=True,
                                on_delete=models.SET_NULL)
    status = models.ForeignKey(Status)
    supplier = models.ManyToManyField(Supplier)
    image = models.ManyToManyField(Image, blank=True)
    upc = models.IntegerField(blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=100, blank=True)
    msrp = models.FloatField(default=0)

    def __str__(self):
        return self.product.name
        # return str(self.id)


class Inventory(models.Model):
    product = models.OneToOneField(ProductVariant)
    quantity_on_hand = models.IntegerField(default=0)

    def __str__(self):
        return self.product.product.name
        # return str(self.id)


