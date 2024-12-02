from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length= 200 , unique = True)
    def __str__(self) : 
        return self.name
class Product(models.Model) : 
    name = models.CharField(max_length= 200 , unique = True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category , related_name= "products" ,  on_delete= models.CASCADE)
    def __str__(self) : 
        return self.name


