from django.shortcuts import render
from .models import Product


def store_home(request):
    products = Product.objects.filter(is_available=True)

    return render(
        request,
        "store-templates/store_home.html",
        {
            "products": products
        }
    )
