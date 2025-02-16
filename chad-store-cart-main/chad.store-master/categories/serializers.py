from rest_framework import serializers
from categories.models import Category, CategoryImage
from products.serializers import ProductSerializer

class CategorySerializer(serializers.Modelserializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CategoryImageSerializer(serializers.Modelserializer):
    class Meta:
        model = CategoryImage  
        fields = ['id', 'image', 'category', 'is_active']
        
class CategoryDetailSerializer(serializers.Modelserializer):
    products = ProductSerializer(many=True, read_only=True)
    images = CategoryImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category 
        fields = ['id', 'name', 'products', 'images'] 