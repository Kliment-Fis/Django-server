from django.shortcuts import render
from products.models import ProductCategory, Product

# Create your views here.


def index(requests):
    context = {
        'title': 'store'
    }
    return render(requests, "products/index.html", context)


def products(requests):
    context = {
        'title': 'store - каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all()
    }
    return render(requests, "products/products.html", context)

