from django.forms import ModelForm
from inventory.models import Image, Category, Subcategory


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image_file', 'thumbnail_file', 'image_alt_text']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']



class SubCategoryForm(ModelForm):
    class Meta:
        model = Subcategory
        fields = ['category', 'name', 'description', 'image']


