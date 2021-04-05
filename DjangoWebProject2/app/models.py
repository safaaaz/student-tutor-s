"""
Definition of models.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class student(models.Model):
    
    ids= models.IntegerField()
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()

    pic=models.ImageField()

    def __str__(self):
        return self.name

class tutor(AbstractUser):
    pass
    idt=models.IntegerField(default=00)
    username=models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=20,default='')
    password=models.CharField(max_length=20)
    age=models.IntegerField(default=00)
    gender=models.CharField(max_length=10,default='')
    price=models.IntegerField(default=45)
    field=models.FileField()
    image=models.ImageField()
    email=models.EmailField()
    phone=models.IntegerField(default=00)


    def __str__(self):
        return self.name 

class course(models.Model):
    tutor = models.ManyToManyField(tutor)
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
