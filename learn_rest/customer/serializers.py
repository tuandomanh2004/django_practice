from .models import Customer , Post
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer) :
    post = serializers.PrimaryKeyRelatedField(many = True , queryset = Post.objects.all())
    class Meta : 
        model = Customer
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer) :
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta : 
        model = Post
        fields = '__all__'