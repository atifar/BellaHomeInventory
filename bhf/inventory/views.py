from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CategoryForm, ColorForm, ImageForm, ProductForm, \
    ProductVariantForm, SizeForm, StatusForm, SubcategoryForm, SupplierForm
from .models import Category, Color, Image, Product, ProductVariant, Size, \
    Status, Subcategory, Supplier


@login_required(login_url='/login')
def homepage(request):
    """Builds a dashboard with inventory summary."""
# Counts list contains the number of inventory items for the summary.
    counts = {}
    counts['category_count'] = Category.objects.count()
    counts['subcategory_count'] = Subcategory.objects.count()
    counts['product_count'] = Product.objects.count()
    counts['prod_var_count'] = ProductVariant.objects.count()
    return render(request, 'index.html', counts)


@login_required(login_url='/login')
def list_products(request):
    """Lists products with some key attributes."""
    product_list = ProductVariant.objects.order_by('product__name')
    context = {'product_list': product_list}
    return render(request, 'list_products.html', context)


@login_required(login_url='/login')
def new_product(request):
    """Add a new product and define all its attributes."""
    # Check if a POST has been submitted.
    if request.POST:
        # Generate the product and product variant forms.
        prod_form = ProductForm(request.POST)
        prodv_form = ProductVariantForm(request.POST)
        # If the form data is valid, save it.
        if prod_form.is_valid() and prodv_form.is_valid():
            updated_prod = prod_form.save()
            updated_prod_var = prodv_form.save(commit=False)
            updated_prod_var.product = updated_prod
            updated_prod_var.save()
            prodv_form.save_m2m()
            return redirect('product_list')
    # If this view was called upon a GET, render the form.
    else:
        prod_form = ProductForm()
        prodv_form = ProductVariantForm()
    return render(request, 'new_product.html', {'prod_form': prod_form,
                                                'prodv_form': prodv_form})


@login_required(login_url='/login')
def edit_product(request, prod_var_id):
    """Edit all attributes of a product."""
    # Fetch the product and product variant objects to edit.
    prod_var = get_object_or_404(ProductVariant, pk=prod_var_id)
    product = prod_var.product
    # Check if a POST has been submitted.
    if request.POST:
        # Generate the product and product variant forms.
        prod_form = ProductForm(request.POST, instance=product)
        prodv_form = ProductVariantForm(request.POST, instance=prod_var)
        # If the form data is valid, save it.
        if prod_form.is_valid() and prodv_form.is_valid():
            updated_prod = prod_form.save()
            updated_prod_var = prodv_form.save(commit=False)
            updated_prod_var.product = updated_prod
            updated_prod_var.save()
            prodv_form.save_m2m()
            return redirect('product_list')
    # If this view was called upon a GET, render the form.
    else:
        prod_form = ProductForm(instance=product)
        prodv_form = ProductVariantForm(instance=prod_var)
    return render(request, 'edit_product.html', {'prod_var': prod_var,
                                                 'product': product,
                                                 'prod_form': prod_form,
                                                 'prodv_form': prodv_form})


@login_required(login_url='/login')
def list_categories(request):
    """Lists categories with some key attributes."""
    category_list = Category.objects.order_by('name')
    context = {'category_list': category_list}
    return render(request, 'list_categories.html', context)


@login_required(login_url='/login')
def new_category(request):
    """Add new category and define all its attributes."""
    # Check if a POST has been submitted.
    if request.POST:
        # Generate the category form.
        cat_form = CategoryForm(request.POST)
        # If the form data is valid, save it.
        if cat_form.is_valid():
            cat_form.save()
            return redirect('category_list')
    # If this view was called upon a GET, render the form.
    else:
        cat_form = CategoryForm()
    return render(request, 'new_category.html', {'cat_form': cat_form})


@login_required(login_url='/login')
def edit_category(request, category_id):
    """Edit all attributes of a category."""
    # Fetch the category object to edit.
    category = get_object_or_404(Category, pk=category_id)
    # Check if a POST has been submitted.
    if request.POST:
        # Generate the category form.
        cat_form = CategoryForm(request.POST, instance=category)
        # If the form data is valid, save it.
        if cat_form.is_valid():
            cat_form.save()
            return redirect('category_list')
    # If this view was called upon a GET, render the form.
    else:
        cat_form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'cat_form': cat_form,
                                                  'category': category})


@login_required(login_url='/login')
def list_subcategories(request, category_id):
    """Lists subcategories with some key attributes."""
    category = get_object_or_404(Category, pk=category_id)
    subcategory_list = category.subcategory_set.order_by('name')
    context = {'category': category, 'subcategory_list': subcategory_list}
    return render(request, 'list_subcategories.html', context)


@login_required(login_url='/login')
def new_subcategory(request, category_id):
    """Add new subcategory and define all its attributes."""
    # category = get_object_or_404(Category, pk=category_id)
    # Check if a POST has been submitted.
    if request.POST:
        # Generate the subcategory form.
        subcat_form = SubcategoryForm(request.POST)
        # If the form data is valid, save it.
        if subcat_form.is_valid():
            subcat_form.save()
            return redirect('subcategory_list', category_id)
    # If this view was called upon a GET, render the form.
    else:
        subcat_form = SubcategoryForm()
    return render(request, 'new_subcategory.html',
                  {'subcat_form': subcat_form, 'category_id': category_id})


@login_required(login_url='/login')
def edit_subcategory(request, category_id, subcategory_id):
    """Edit all attributes of a subcategory."""
    category = get_object_or_404(Category, pk=category_id)
    subcategory = category.subcategory_set.get(pk=subcategory_id)
    # Check if a POST has been submitted.
    if request.POST:
        # Generate the subcategory form.
        subcat_form = SubcategoryForm(request.POST, instance=subcategory)
        # If the form data is valid, save it.
        if subcat_form.is_valid():
            subcat_form.save()
            return redirect('subcategory_list', category_id)
    # If this view was called upon a GET, render the form.
    else:
        subcat_form = SubcategoryForm(instance=subcategory)
    return render(request, 'edit_subcategory.html',
                  {'subcat_form': subcat_form, 'category_id': category_id,
                   'subcategory': subcategory})
