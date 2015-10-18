from django.conf.urls import url
from inventory.views import list_products


urlpatterns = [
    url(r'^products/', list_products, name='product_list_view'),
]
