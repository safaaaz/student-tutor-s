"""
Definition of models.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime

#User = settings.AUTH_USER_MODEL

# Create your models here.


class course(models.Model):
    
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'course'



class tutor(User):

    #user_ptr = models.ForeignKey(User,on_delete='')
    idt=models.IntegerField(default=00)
    #username=models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=20,default='')
    #password=models.CharField(max_length=20)
    age=models.IntegerField(default=00)
    gender=models.CharField(max_length=10,default='')
    price=models.IntegerField(default=45)
    #courses = models.ManyToManyField(course)
    field=models.FileField()
    image=models.ImageField()
    #email=models.EmailField()
    phone=models.IntegerField(default=00)
    is_ok= models.BooleanField(default=False)
    courses=models.CharField(max_length=100,default='')
    coursees = models.ManyToManyField(course)
    


    def __str__(self):
        return self.name
    class Meta:
        db_table = 'tutors'


class student(User):
    
    ids= models.IntegerField()
    name=models.CharField(max_length=50)
    #password=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    #email=models.CharField(max_length=50)
    phone=models.IntegerField()
    #chart = models.ManyToManyField(tutor,through='cart')
    pic=models.ImageField()
    #tutors = models.ManyToManyField(tutor)


    def __str__(self):
        return self.name
    class Meta:
        db_table = 'students'


class cart(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    tutor=models.ForeignKey(tutor, on_delete=models.CASCADE)
    date_shop = models.DateField(default=datetime.now)
    courses=models.ManyToManyField(course)
    numlessons=models.IntegerField(default=1)
    price=models.IntegerField()
    done=models.BooleanField(default=False)

    
       


