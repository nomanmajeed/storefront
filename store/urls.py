from django.urls import path

from store.views import products_list, product_detail

urlpatterns = [
    path('products/', products_list, name="products-list"),
    path('product/<int:id>', product_detail, name="product-detail"),
]