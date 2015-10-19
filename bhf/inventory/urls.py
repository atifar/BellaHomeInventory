from django.conf.urls import url
from inventory.views import list_products, edit_product, list_categories, \
    edit_category, new_category, list_subcategories, edit_subcategory, \
    new_subcategory


urlpatterns = [
    url(r'^$', list_products),
    url(r'^product/$', list_products, name='product_list'),
    # url(r'^product/new/$', new_product, name='new_product'),
    url(r'^product/(?P<prod_var_id>[0-9]+)/$', edit_product,
        name='edit_product'),
    url(r'^category/$', list_categories, name='category_list'),
    url(r'^category/new$', new_category, name='new_category'),
    url(r'^category/(?P<category_id>[0-9]+)/$', edit_category,
        name='edit_category'),
    url(r'^category/(?P<category_id>[0-9]+)/subcategory/new$', new_subcategory,
        name='new_subcategory'),
    url(r'^category/(?P<category_id>[0-9]+)/subcategory/$', list_subcategories,
        name='subcategory_list'),
    url(r'^category/(?P<category_id>[0-9]+)/subcategory/(?P<subcategory_id>[0-9]+)/$',
        edit_subcategory, name='edit_subcategory'),
]
