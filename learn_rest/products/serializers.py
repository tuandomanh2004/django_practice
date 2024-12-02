from rest_framework import serializers
from .models import Product , Category

class ProductSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer) : 
    products = serializers.PrimaryKeyRelatedField(many = True , queryset = Product.objects.all())
    class Meta : 
        model = Category
        fields = '__all__'