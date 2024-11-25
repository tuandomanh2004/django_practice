from django.db import models

class Post(models.Model) : 
    title = models.TextField(max_length= 200 , unique= True)
    content = models.TextField(unique = True)
    author = models.ForeignKey('auth.User' , on_delete = models.CASCADE)
    def __str__(self) : 
        return self.title
