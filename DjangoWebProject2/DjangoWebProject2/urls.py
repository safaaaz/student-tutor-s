"""
Definition of urls for DjangoWebProject2.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app import forms, views


admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('show/', views.show, name='show'),
   # path('login/s', views.s, name='s'),
   # path('totur/s',views.s,name='s'),

    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         views.login
         #(
             #template_name='app/login.html',
             #authentication_form=forms.BootstrapAuthenticationForm,
             #extra_context=
             #{
             #    'title': 'Log in',
             #    'year' : datetime.now().year,
             #}
         #),
         ,name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('app/signup', views.signup_view, name='signup'),

    #path('app/login', auth_views.LoginView.as_view(), name='login'),
    path('app/login_page', views.login_page, name='signup'),
    
    path('app/studentsignup', views.studentsignup, name='studentsignup'),
    path('app/profile', views.profile.as_view(template_name='app/profile.html'), name='profile'),

]
