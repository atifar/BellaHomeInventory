__author__ = 'Ati'

import factory
from . import models


class ImageFactory(factory.DjangoModelFactory):
    """
    Uses an existing Image instance, or creates a new one.

    By default, the first 16 created instances are generated solid color
    images and thumbnails using distinct colors.
    """
    class Meta:
        model = models.Image
        exclude = ('color',)
        django_get_or_create = ('image_file','thumbnail_file')

    color = factory.Iterator(
        ['tan', 'blue', 'green', 'gray', 'red', 'black', 'aqua', 'beige',
         'coral', 'indigo', 'lime', 'plum', 'olive', 'peru', 'teal', 'orange'])
    image_file = factory.django.ImageField(color=color, width=300,
                                           height=300,
                                           filename='{}_big.jpg'.format(color))
    thumbnail_file = factory.django.ImageField(color=color, width=100,
                                               height=100,
                                               filename='{}_sml.jpg'.format(
                                                   color))
    image_alt_text = '{} image.'.format(color)


class CategoryFactory(factory.DjangoModelFactory):
    """Creates an instance of the Category model."""
    class Meta:
        model = models.Category
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'Quilts #{}'.format(str(n)))
    description = factory.LazyAttribute(
        lambda o: 'Wonderful products in {}.'.format(o.name))

    @factory.post_generation
    def image(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing!
            return

        if extracted:
            # A list of images was passed in, add them!
            for img in extracted:
                self.image.add(img)


