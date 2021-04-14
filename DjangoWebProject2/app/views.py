"""
Definition of views.
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import datetime
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
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from app.models import tutor
from django.shortcuts import render
from .models import tutor
from django.contrib import admin


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    stu = tutor.objects.all()
    return render(
        request,
        'app/index.html',
       {'stu':stu}
    )

def show(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    stu = tutor.objects.get(name='3339')
    return render(
        request,
        'app/show.html',
       {'stu':stu}
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

def s(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/s.html',
        {
            'title':'the toturs:',
            'message':'ok',
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
        form = studentForm(request.POST, request.FILES)
        #print(form.errors)
        if form.is_valid():
            form.save()
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('app/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'Your account has been created ! You are now able to log in')
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
   

def login(request):
    if request.user.is_authenticated:
        return render(request, 'app/index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #k=student.objects.all()
        if user is not None:
            auth_login(request,user)
            if student.objects.filter(username=user.username):
                
                return redirect('home')
            elif tutor.objects.filter(username=user.username):
                return render(request, 'app/tutorpage.html')
            else:
                return HttpResponseRedirect('admin')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'app/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'app/login.html', {'form': form})



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

