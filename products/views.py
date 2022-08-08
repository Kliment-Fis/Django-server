from django.shortcuts import render

# Create your views here.


def index(requests):
    context = {
        "title": 'store'
    }
    return render(requests, "products/index.html", context)


def products(requests):
    context = {
        "title": 'store - каталог'
    }
    return render(requests, "products/products.html", context)

