"""
Definition of models.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import django_filters 
from django_filters import FilterSet
from .models import *
from datetime import datetime



#User = settings.AUTH_USER_MODEL

# Create your models here.
class message(models.Model):
    
    title=models.CharField(max_length=90)
    content=models.CharField(max_length=300)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'message'

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
    image=models.ImageField(upload_to='images', null=True, verbose_name="")
    email0=models.EmailField(null=True)
    phone=models.IntegerField(default=00)
    is_ok= models.BooleanField(default=False)
    courses=models.CharField(max_length=100,default='')
    coursees = models.ManyToManyField(course)
    rate=models.IntegerField(default=00)
    messages = models.ManyToManyField(message)
    def __str__(self):
        return self.name +' ' + self.last_name
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
    #chart = models.ManyToManyField(tutor)
    pic=models.ImageField()
    #tutors = models.ManyToManyField(tutor)


    def __str__(self):
        return self.name
    class Meta:
        db_table = 'students'

        
class ProductFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    rate = django_filters.NumberFilter()
    rate__gt = django_filters.NumberFilter(field_name='rate', lookup_expr='gt')
    rate__lt = django_filters.NumberFilter(field_name='rate', lookup_expr='lt')
    manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = tutor
        fields = ['price','rate']

class cart(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    tutor=models.ForeignKey(tutor, on_delete=models.CASCADE)
    date_shop = models.DateField(default=datetime.now)
    courses=models.ManyToManyField(course)
    numlessons=models.IntegerField(default=1)
    price=models.IntegerField()
    done=models.BooleanField(default=False)

    
       


