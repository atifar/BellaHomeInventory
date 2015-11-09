from django.forms import CheckboxInput, ModelForm, NumberInput, Select, \
    SelectMultiple, Textarea, TextInput
from inventory.models import Category, Color, Image, Product, ProductVariant, \
    Size, Status, Subcategory, Supplier


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        widgets = {
            'name': TextInput(attrs={'class': "form-control",
                                     'placeholder': "Category name"}),
            'description': Textarea(attrs={'rows': 4, 'class': "form-control",
                                           'placeholder': "Category description"}),
            'image': SelectMultiple(attrs={'class': "form-control"}),
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
        widgets = {
            'name': TextInput(attrs={'class': "form-control",
                                     'placeholder': "Product name"}),
            'description': Textarea(attrs={'rows': 4, 'class': "form-control",
                                           'placeholder': "Product description"}),
            'short_description': Textarea(
                attrs={'rows': 4, 'class': "form-control",
                       'placeholder': "Product short description"}),
            'category': SelectMultiple(attrs={'class': "form-control"}),
            'subcategory': SelectMultiple(attrs={'class': "form-control"}),
        }


class ProductVariantForm(ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['product', 'color', 'size', 'status', 'supplier', 'image',
                  'upc', 'weight', 'code', 'msrp', 'special_order',
                  'quantity_on_hand']
        exclude = ['product']
        widgets = {
            'color': Select(attrs={'class': "form-control"}),
            'size': Select(attrs={'class': "form-control"}),
            'status': Select(attrs={'class': "form-control"}),
            'supplier': SelectMultiple(attrs={'class': "form-control"}),
            'image': SelectMultiple(attrs={'class': "form-control"}),
            'upc': NumberInput(attrs={'class': "form-control"}),
            'weight': TextInput(attrs={'class': "form-control",
                                       'placeholder': "Item weight"}),
            'code': TextInput(attrs={'class': "form-control",
                                     'placeholder': "Internal code"}),
            'msrp': NumberInput(attrs={'class': "form-control"}),
            'quantity_on_hand': NumberInput(attrs={'class': "form-control"}),
            'special_order': CheckboxInput(attrs={'class': "form-control"}),
        }


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
            'category': Select(attrs={'class': "form-control"}),
            'name': TextInput(attrs={'class': "form-control",
                                     'placeholder': "Category name"}),
            'description': Textarea(attrs={'rows': 4, 'class': "form-control",
                                           'placeholder': "Category description"}),
            'image': SelectMultiple(attrs={'class': "form-control"}),
        }


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'address2', 'city', 'state', 'zip',
                  'phone', 'fax', 'email']

