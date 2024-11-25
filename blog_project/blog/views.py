from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post
class ListPost(ListView)  :
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
class DetailPost(DetailView) : 
    model = Post
    template_name = 'detail.html'