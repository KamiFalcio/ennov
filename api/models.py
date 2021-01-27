from django.db import models

# Create your models here.
class Hcpro(models.Model):
    firstname = models.CharField(max_length= 30)
    lastname = models.CharField(max_length= 30)
    email = models.CharField(max_length= 200, unique= True)
    postal_adress = models.IntegerField(null= True)
    isDeleted = models.BooleanField(default= False)
    def __str__(self):
        return self.lastname