from django.shortcuts import render
from rest_framework import generics , permissions
from .models import Customer , Post
from .serializers import CustomerSerializer , PostSerializer
from .permissions import IsOwnerOrReadOnly
class CustomerList(generics.ListCreateAPIView) : 
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView) : 
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PostList(generics.ListCreateAPIView) : 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
       serializer.save(owner = self.request.user)
class PostDetail(generics.RetrieveUpdateDestroyAPIView) : 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer