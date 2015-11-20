from django.core.validators import MinValueValidator
from django.forms import CheckboxInput, ModelForm, NumberInput, Select, \
    SelectMultiple, Textarea, TextInput
from inventory.models import Category, Color, Image, Product, ProductVariant, \
    Size, Status, Subcategory, Supplier


class CategoryForm(ModelForm):
    """Form configuration for category model."""
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        # Attributes, including "form-control" class for Bootstrap styling
        widgets = {
            'name': TextInput(attrs={'class': "form-control",
                                     'placeholder': "Category name"}),
            'description':
                Textarea(attrs={'rows': 4,
                                'class': "form-control",
                                'placeholder': "Category description"}),
            'image': SelectMultiple(attrs={'class': "form-control"}),
        }


class ColorForm(ModelForm):
    """Form configuration for color model."""
    class Meta:
        model = Color
        fields = ['color']


class ImageForm(ModelForm):
    """Form configuration for image model."""
    class Meta:
        model = Image
        fields = ['image_file', 'thumbnail_file', 'image_alt_text']


class ProductForm(ModelForm):
    """Form configuration for product model."""
    class Meta:
        model = Product
        fields = ['name', 'description', 'short_description', 'category',
                  'subcategory']
        # Attributes, including "form-control" class for Bootstrap styling
        widgets = {
            'name': TextInput(attrs={'class': "form-control",
                                     'placeholder': "Product name"}),
            'description':
                Textarea(attrs={'rows': 4,
                                'class': "form-control",
                                'placeholder': "Product description"}),
            'short_description': Textarea(
                attrs={'rows': 4, 'class': "form-control",
                       'placeholder': "Product short description"}),
            'category': SelectMultiple(attrs={'class': "form-control"}),
            'subcategory': SelectMultiple(attrs={'class': "form-control"}),
        }


class ProductVariantForm(ModelForm):
    """Form configuration for product variant model."""
    def __init__(self, *args, **kwargs):
        super(ProductVariantForm, self).__init__(*args, **kwargs)

        # Adding MinValueValidator(0) to prevent negative 'upc' values.
        validators = [v for v in self.fields['upc'].validators if
                      not isinstance(v, MinValueValidator)]
        validators.append(MinValueValidator(0))
        self.fields['upc'].validators = validators

        # Adding MinValueValidator(0) to prevent negative 'msrp' values.
        validators = [v for v in self.fields['msrp'].validators if
                      not isinstance(v, MinValueValidator)]
        validators.append(MinValueValidator(0))
        self.fields['msrp'].validators = validators

        # Adding MinValueValidator(0) to prevent negative 'quantity_on_hand'
        # values.
        validators = [v for v in self.fields['quantity_on_hand'].validators if
                      not isinstance(v, MinValueValidator)]
        validators.append(MinValueValidator(0))
        self.fields['quantity_on_hand'].validators = validators

    class Meta:
        model = ProductVariant
        fields = ['product', 'color', 'size', 'status', 'supplier', 'image',
                  'upc', 'weight', 'code', 'msrp', 'special_order',
                  'quantity_on_hand']
        exclude = ['product']
        # Attributes, including "form-control" class for Bootstrap styling
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
    """Form configuration for size model."""
    class Meta:
        model = Size
        fields = ['size_code', 'width', 'length', 'depth']


class StatusForm(ModelForm):
    """Form configuration for status model."""
    class Meta:
        model = Status
        fields = ['status']


class SubcategoryForm(ModelForm):
    """Form configuration for subcategory model."""
    class Meta:
        model = Subcategory
        fields = ['category', 'name', 'description', 'image']
        # Attributes, including "form-control" class for Bootstrap styling
        widgets = {
            'category': Select(attrs={'class': "form-control"}),
            'name': TextInput(attrs={'class': "form-control",
                                     'placeholder': "Category name"}),
            'description':
                Textarea(attrs={'rows': 4,
                                'class': "form-control",
                                'placeholder': "Category description"}),
            'image': SelectMultiple(attrs={'class': "form-control"}),
        }


class SupplierForm(ModelForm):
    """Form configuration for supplier model."""
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'address2', 'city', 'state', 'zip',
                  'phone', 'fax', 'email']
