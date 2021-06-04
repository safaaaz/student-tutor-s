

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



from django_filters.views import object_filter
admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('show/', views.show, name='show'),
    path('template/', views.product_list,name='template'),
    path('app/updatestud', views.updatestud, name='updatestud'),
   
     path('CheckOut/', views.CheckOut, name='CheckOut'),
     path('show/CheckOut', views.CheckOut, name='CheckOut1'),
   # path('login/s', views.s, name='s'),
   # path('totur/s',views.s,name='s'),
    path('Search/', views.home, name='Search'),
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
    path('contact/sendtomanager', views.sendtomanager, name='sendtomanager'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/admin', admin.site.urls),
    path('admin', admin.site.urls),
    path('app/signup', views.signup_view, name='signup'),
    path('search/', views.search_tutor, name='search'),
    #path('app/login', auth_views.LoginView.as_view(), name='login'),
    path('app/login_page', views.login_page, name='login_page'),
    path('show/addchart', views.addchart, name='addchart'),
    path('show/show/addchart', views.addchart, name='addchart1'),
   # path('show/ratings', views.ratings, name='ratings'),
    
    path('login/tutorstud', views.tutorstud, name='tutorstud'),
    path('login/messagest', views.messagest, name='messagest'),
    path('show/rate1', views.rate1, name='rate1'),
    path('show/rate2', views.rate2, name='rate2'),
    path('show/rate3', views.rate3, name='rate3'),
    path('show/rate4', views.rate4, name='rate4'),
    path('show/rate5', views.rate5, name='rate5'),

    path('messagest', views.messagest, name='messagest1'),
    path('CheckOut/buy', views.buy, name='buy'),
    path('show/buy', views.buy, name='buy1'),
    path('show/back', views.back, name='back'),
    path('show/show/back', views.back, name='back1'),
    path('show/show/',views.show, name='show1'),
    path('show/ourcart', views.ourcart, name='ourcart'),
    path('app/studentsignup', views.studentsignup, name='studentsignup'),
    path('app/profile', views.prof, name='profile'),
    path('CheckOut/deleteitem',views.deleteitem, name='deleteitem'),
    path('show/deleteitem',views.deleteitem, name='deleteitem1'),

    path('app/changet',views.changet, name='changet'),
    ###################################################################33
   # path('app/', include('django.contrib.auth.urls')),
 path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),  
 path("password_reset", auth_views.PasswordResetView.as_view(template_name='app/password_reset.html'), name="password_reset"),
     path('app/deleteuser', views.deleteuser, name='deleteuser'),
     ]+ static(settings.MEDIA_URL, document_root= settings.STATIC_MEDIA)
 

#urlpatterns = [
  #  path('r/admin/', admin.site.urls),
  #  path('r/accounts/', include('registration.backends.default.urls')),
  #  path('', include('social.apps.django_app.urls', namespace='social')),
   # path('r/Blog/', include('Blog.urls')),
   # path('r/growth/', include('growth.urls')),
    
#] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



