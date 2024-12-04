from django.urls import path
from .views import CustomerList , CustomerDetail , PostDetail , PostList
urlpatterns = [
    path('customer/' , CustomerList.as_view() , name = 'customer_list') , 
    path('customer/<int:pk>/' , CustomerDetail.as_view() , name = 'customer_detail'),
    path('posts/' , PostList.as_view() , name = 'post_list'),
    path('posts/<int:pk>/' , PostDetail.as_view() , name = 'post_detail')
]
