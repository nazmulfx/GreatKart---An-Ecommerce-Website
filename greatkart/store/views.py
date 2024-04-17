from django.shortcuts import render, get_object_or_404

from . models import Product
from category.models import Category
# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
        totalProduct = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        totalProduct = products.count()
    
    context = {'products':products, 'totalProduct':totalProduct}
    return render(request, 'store/store.html', context)


def product_details(request, category_slug, product_slug):
    
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context = {'product':product}
    return render(request, 'store/product_details.html', context)