from django.conf.urls import url
from inventory.views import ProductListView


urlpatterns = [
    url(r'^products/', ProductListView.as_view(), name='product_list_view'),
]
