# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.http import HttpResponse
from django.shortcuts import render
# from django.views.generic import ListView
from .models import ProductVariant


def list_products(request):
    product_list = ProductVariant.objects.all()
    context = {'product_list': product_list}
    return render(request, 'list_products.html', context)


# class ProductListView(ListView):
#     model = ProductVariant
#     template_name = 'list_products.html'
#     context_object_name = 'cust_products'
#     # queryset = ProductVariant.objects.all()
#
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductListView, self).get_context_data(**kwargs)
#         cust_products = {}
#         for i, product in enumerate(ProductVariant.objects.all()):
#             img = product.image.all()[0]
#             cust_products[i] = {
#                 'thumb': img.thumbnail_file.url,
#                 'name': product.product.name,
#                 'color': product.color,
#                 'status': product.status
#             }
#             print(cust_products[i]['thumb'])
#         # context['img'] = cust_products
#         return context


    # def get(self, request, *args, **kwargs):
    #
    #     return HttpResponse()

    # Use the following code when user login is to be enforced
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(ProductListView, self).dispatch(*args, **kwargs)

