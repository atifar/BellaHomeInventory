from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ProductVariant


@login_required(login_url='/login')
def list_products(request):
    product_list = ProductVariant.objects.all()
    context = {'product_list': product_list}
    return render(request, 'list_products.html', context)


