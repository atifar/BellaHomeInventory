from django.contrib import admin

from .models import Image, Category, Subcategory, Color, Size, Status
from .models import Supplier, Product, ProductVariant, Inventory

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Status)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(Inventory)
