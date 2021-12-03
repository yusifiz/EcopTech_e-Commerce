from django.shortcuts import render

# Create your views here.

def products_on_sale(request):
    return render(request, "products-on-sale.html")

def shop(request):
    return render(request, "shop.html")

def single_product(request):
    return render(request, "single-product.html")