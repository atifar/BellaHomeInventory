from django.db import models


def upload_handler(instance, filename):
    """Returns the relative file path for user uploaded images."""
    return 'img/{}'.format(filename)


class Image(models.Model):
    """Model definition for images."""
    image_file = models.ImageField(upload_to=upload_handler, blank=True)
    thumbnail_file = models.ImageField(upload_to=upload_handler, blank=True)
    image_alt_text = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.image_alt_text


class Category(models.Model):
    """Model definition for categories."""
    image = models.ManyToManyField(Image)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1200)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """Model definition for subcategories."""
    image = models.ManyToManyField(Image)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1200)

    def __str__(self):
        return self.name


class Color(models.Model):
    """Model definition for colors."""
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color


class Size(models.Model):
    """Model definition for sizes."""
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
    """Model definition for status."""
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class Supplier(models.Model):
    """Model definition for suppliers."""
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    phone = models.BigIntegerField(blank=True, null=True)
    fax = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model definition for products."""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    short_description = models.TextField(max_length=250, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    subcategory = models.ManyToManyField(Subcategory, blank=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    """Model definition for product variants."""
    product = models.ForeignKey(Product)
    color = models.ForeignKey(Color)
    size = models.ForeignKey(Size)
    status = models.ForeignKey(Status)
    supplier = models.ManyToManyField(Supplier)
    image = models.ManyToManyField(Image, blank=True)
    special_order = models.BooleanField(default=False)
    upc = models.IntegerField(blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=100, blank=True)
    msrp = models.FloatField(default=0)
    quantity_on_hand = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name
