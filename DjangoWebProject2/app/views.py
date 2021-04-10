"""
Definition of views.
"""
from django.urls import reverse_lazy
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from .models import tutor,student
from .forms import tutorForm,studentForm,tutorChangeForm,studentChangeForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def signup1(request):
     form = tutorForm()
     if request.method=='POST':
        form=tutorForm(request.POST, request.FILES)
        #print(form.errors)
        if form.is_valid():
            
            form.save()
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('about')
     return render(request,'app/signup.html',{'form':form})

def signup_view(request):
    form = tutorForm()
    if request.method=='POST':
        form=tutorForm(request.POST, request.FILES)
        #print(form.errors)
        if form.is_valid():
            
            form.save()
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('about')
    context ={'form':form}
    
    return render(request, 'app/signup.html',context)   

def studentsignup(request):
    form = studentForm()
    if request.method=='POST':
        form=studentForm(request.POST, request.FILES)
        #print(form.errors)
        if form.is_valid():
            form.save()
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('about')
    context ={'form':form}
    
    return render(request, 'app/studentsignup.html',context) 


#@login_required
#def profile(request):
#    #form = tutorChangeForm(request)

#            #user = authenticate(username=username, password=raw_password)
#            #login(request, user)
#           # return redirect('about')
#    if request.method=='POST':
#            form = tutorChangeForm(request.POST,instance=request.User)
#    #       p_form = profileupform(request.POST,request.FILES,instance=request.User.profile)
#            if form.is_valid():
#                 form.save()
#    #            p_form.save()
#    #            messages.success(request, 'Your account has been updated!')
#                 return redirect('profile')
#    else:
#            form = tutorChangeForm(instance=request.user)
#    #       p_form = profileupform(instance=request.user)
#            context ={'form':form}
#            return render(request,'app/profile.html',context)

#class studentprofile(UpdateView):
#    model = student
#    form = studentChangeForm
#    template_name = 'profile.html'
#    fields = ['email','age','phone','pic']
#    success_url = reverse_lazy('home') # This is where the user will be 
#                                       # redirected once the form
#                                       # is successfully filled in

#    def get_object(self, **kwargs):
#        '''This method will load the object
#           that will be used to load the form
#           that will be edited'''
#        return self.request.user
   


class profile(UpdateView):
    model = tutor
    form = tutorChangeForm
    template_name = 'profile.html'
    fields = ['email','price','age','phone']

    success_url = reverse_lazy('home') # This is where the user will be 
                                       # redirected once the form
                                       # is successfully filled in

    def get_object(self, **kwargs):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        return self.request.user
   
def login_page(request):

    return render(request,'app/login_page.html')