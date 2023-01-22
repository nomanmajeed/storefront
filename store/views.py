from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import *
from store.serializers import ProductSerializer, ProductMSerializer, CollectionSerializer

# Create your views here.

@api_view()
def collection_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = CollectionSerializer(product)
    return Response(serializer.data)

@api_view()
def products_list(request):
    products = Product.objects.select_related('collection').all()
    # serializer = ProductSerializer(products, many=True, context={'request': request})
    serializer = ProductMSerializer(products, many=True, context={'request': request})
    return Response(serializer.data)

@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    # serializer = ProductSerializer(product)
    serializer = ProductMSerializer(product, context={'request': request})
    return Response(serializer.data)