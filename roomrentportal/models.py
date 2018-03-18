from django.db import models

# Create your models here
class UserModel(models.Model):
    name=models.CharField(max_length=500)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=15)

    def __str__(self):
        return '%s %s '%(self.name,self.email)

