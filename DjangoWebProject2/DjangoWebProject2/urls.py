"""
Definition of urls for DjangoWebProject2.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app import forms, views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include



admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('show/', views.show, name='show'),
    path('search/', views.search_tutor, name='search'),
     path('CheckOut/', views.CheckOut, name='CheckOut'),
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
    path('login/admin', admin.site.urls),
    path('app/signup', views.signup_view, name='signup'),

    #path('app/login', auth_views.LoginView.as_view(), name='login'),
    path('app/login_page', views.login_page, name='signup'),
    path('show/addchart', views.addchart, name='addchart'),
    path('app/studentsignup', views.studentsignup, name='studentsignup'),
    path('app/profile', views.profile, name='profile'),
    ###################################################################33
   # path('app/', include('django.contrib.auth.urls')),
 path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),  
 path("password_reset", auth_views.PasswordResetView.as_view(template_name='app/password_reset.html'), name="password_reset"),
     path('app/deleteuser', views.deleteuser, name='deleteuser'),

 

#urlpatterns = [
  #  path('r/admin/', admin.site.urls),
  #  path('r/accounts/', include('registration.backends.default.urls')),
  #  path('', include('social.apps.django_app.urls', namespace='social')),
   # path('r/Blog/', include('Blog.urls')),
   # path('r/growth/', include('growth.urls')),
    
#] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


]+ static(settings.MEDIA_URL, document_root= settings.STATIC_MEDIA)

