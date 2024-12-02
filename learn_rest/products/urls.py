from django.urls import path
from .views import CategoryList,  ProductList , ProductDetail

urlpatterns = [
    path('category/' , CategoryList.as_view() , name = 'category'),
    path('category/products/' , ProductList().as_view() , name = 'product_list'),
    path('category/products/<int:pk>/' ,ProductDetail.as_view() , name = 'product_detail')
]