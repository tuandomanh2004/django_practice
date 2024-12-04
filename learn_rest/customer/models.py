from django.db import models
from django.contrib.auth.models import User 
class Customer(models.Model) : 
    name = models.CharField(max_length= 100 , unique= True)
    sex = models.BooleanField()
    country = models.CharField(max_length= 200)
    class Meta : 
        ordering = ['name']
    def __str__(self) : 
        return self.name
class Post(models.Model) : 
    post_name = models.CharField(max_length= 200 , default= "")
    content = models.TextField()
    owner = models.ForeignKey( User , related_name = 'post' , on_delete= models.CASCADE )
    def __str__(self) : 
        return self.post_name