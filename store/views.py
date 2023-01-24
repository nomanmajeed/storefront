from django.db.models import Count
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from store.models import *
from store.serializers import ProductSerializer, ProductMSerializer, CollectionSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def collections_list(request):
    if request.method == 'GET':
        collections = Collection.objects.annotate(products_count=Count('products')).all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(
        Collection.objects.annotate(products_count=Count('products')).all(), pk=pk)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if collection.products.count > 0:
            return Response({
                'error':'Collections cannot be deleted because it is associated products with it.'
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.select_related('collection').all()
        serializer = ProductMSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductMSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.user == 'GET':
        serializer = ProductMSerializer(product, context={'request': request})
        return Response(serializer.data)
    elif request.user == 'PUT' or request.user == 'PATCH':
        serializer = ProductMSerializer(product, data=request.data)
        return Response(serializer.data)
    elif request.user == 'DELETE':
        if product.otheritem_set.count > 0:
            return Response({
                'error':'Cannot delete a product because it is associated with a product item.'
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        