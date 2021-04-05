"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



from .forms import tutorForm
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

class SignUpView(CreateView):
    form_class = tutorForm
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'

def login_page(request):

    return render(request,'app/login_page.html')