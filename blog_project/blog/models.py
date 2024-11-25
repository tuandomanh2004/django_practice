from django.db import models
from django.urls import reverse
class Post(models.Model) : 
    title = models.TextField(max_length= 200 , unique= True)
    content = models.TextField(unique = True)
    author = models.ForeignKey('auth.User' , on_delete = models.CASCADE)
    def get_absolute_url(self) : 
        return reverse('detail' , args = str(self.id))
    def __str__(self) : 
        return self.title
