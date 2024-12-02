from django.shortcuts import render
from rest_framework import generics
from .models import Product , Category
from .serializers import ProductSerializer , CategorySerializer
class ProductList(generics.ListCreateAPIView) : 
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer
    
class CategoryList(generics.ListCreateAPIView) : 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView) : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
 