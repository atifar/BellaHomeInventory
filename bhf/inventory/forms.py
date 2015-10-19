from django.forms import ModelForm, CheckboxSelectMultiple, RadioSelect
from inventory.models import Category, Color, Image, Product, ProductVariant, \
    Size, Status, Subcategory, Supplier


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        widgets = {
            'image': CheckboxSelectMultiple,
        }


class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = ['color']


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image_file', 'thumbnail_file', 'image_alt_text']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'short_description', 'category',
                  'subcategory']


class ProductVariantForm(ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['product', 'color', 'size', 'status', 'supplier', 'image',
                  'special_order', 'upc', 'weight', 'code', 'msrp',
                  'quantity_on_hand']


class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = ['size_code', 'width', 'length', 'depth']


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['status']


class SubcategoryForm(ModelForm):
    class Meta:
        model = Subcategory
        fields = ['category', 'name', 'description', 'image']
        widgets = {
            'category': RadioSelect,
            'image': CheckboxSelectMultiple,
        }


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'address2', 'city', 'state', 'zip',
                  'phone', 'fax', 'email']

