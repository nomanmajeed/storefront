from django.urls import path

from store.views import products_list, product_detail, collection_detail, collections_list

urlpatterns = [
    path('collections/', collections_list, name="collection-list"),
    path('collection/<int:id>', collection_detail, name="collection-detail"),
    path('products/', products_list, name="products-list"),
    path('product/<int:id>', product_detail, name="product-detail"),
]