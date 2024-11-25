from django.urls import path 
from .views import ListPost , DetailPost , UpdatePost , DeletePost , CreatePost

urlpatterns = [
    path('post/new/' , CreatePost.as_view() , name = 'create'),
    path('post/<int:pk>/' , DetailPost.as_view() , name = 'detail'),
    path('post/<int:pk>/edit/' , UpdatePost.as_view() , name = 'edit'),
    path('post/<int:pk>/delete/' , DeletePost.as_view() , name = 'delete'),
    path( '' , ListPost.as_view() , name = 'home')
]