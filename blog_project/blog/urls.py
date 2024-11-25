from django.urls import path 
from .views import ListPost , DetailPost

urlpatterns = [
    path( '' , ListPost.as_view() , name = 'home'),
    path('post/<int:pk>/' , DetailPost.as_view() , name = 'detail')
]