from django.urls import path

from store import views

urlpatterns = [
    path('collections/', views.collections_list, name="collection-list"),
    path('collection/<int:id>', views.collection_detail, name="collection-detail"),
    # path('products/', views.products_list, name="products-list"),
    path('products/', views.ProductList.as_view(), name="products-list"),
    # path('product/<int:id>', views.product_detail, name="product-detail"),
    path('product/<int:id>', views.ProductDetail.as_view(), name="products-detail"),
]