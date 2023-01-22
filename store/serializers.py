from decimal import Decimal

from rest_framework import serializers

from store.models import Product, Collection

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection_pkr = serializers.PrimaryKeyRelatedField(
        queryset=Collection.objects.all(), source='collection'
    )
    collection_str = serializers.StringRelatedField(source='collection')
    collection_hyp = serializers.HyperlinkedRelatedField(
        view_name='collection-detail',
        # queryset=Collection.objects.all(),
        read_only=True,
        lookup_field='id',
        source='collection'
    )
    collection = CollectionSerializer()
    
    def calculate_tax(self, product: Product):
        
        return product.unit_price * Decimal(1.2)
    

class ProductMSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection_pkr = serializers.PrimaryKeyRelatedField(
        queryset=Collection.objects.all(), source='collection'
    )
    collection_str = serializers.StringRelatedField(source='collection')
    collection_hyp = serializers.HyperlinkedRelatedField(
        view_name='collection-detail',
        # queryset=Collection.objects.all(),
        read_only=True,
        lookup_field='id',
        source='collection'
    )
    collection = CollectionSerializer()
    
    def calculate_tax(self, product: Product):
        
        return product.unit_price * Decimal(1.2)
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'price_with_tax', 'collection_pkr', 'collection_str', 'collection_hyp', 'collection']