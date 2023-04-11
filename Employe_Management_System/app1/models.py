from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=12,null=True)
    
    def __str__(self):
        return self.name
