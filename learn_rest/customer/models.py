from django.db import models

class Customer(models.Model) : 
    name = models.CharField(max_length= 100 , unique= True)
    sex = models.BooleanField()
    country = models.CharField(max_length= 200)
    class Meta : 
        ordering = ['name']
    def __str__(self) : 
        return self.name