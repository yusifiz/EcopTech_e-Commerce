from django.urls import path
from .views import products_on_sale, shop, single_product

app_name = 'products'

urlpatterns = [
    path('products-on-sale/', products_on_sale, name='products_on_sale'),
    path('', shop, name='shop'),
    path('single-product/', single_product, name='single_product'),
]