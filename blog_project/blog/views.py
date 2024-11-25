from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView
from .models import Post
from django.urls import reverse_lazy
class ListPost(ListView)  :
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
class DetailPost(DetailView) : 
    model = Post
    template_name = 'detail.html'
class CreatePost(CreateView) : 
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'
class UpdatePost(UpdateView) : 
    model = Post
    template_name = 'update_post.html'
    fields = ['title' , 'content']
class DeletePost(DeleteView) : 
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')