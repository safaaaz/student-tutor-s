"""
Definition of views.
"""
from django.db.models import Q
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
from .models import tutor,student,ProductFilter
from .forms import tutorForm,studentForm,tutorChangeForm,studentChangeForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from app.models import tutor,cart
from django.shortcuts import render
from .models import tutor
from django.contrib import admin
#########################################################
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from django.shortcuts import render
from .models import tutor
#from .forms import ImageForm


from .forms import UserDeleteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from django.core.mail import send_mail

@login_required
def deleteuser(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('home')
    else:
        delete_form = UserDeleteForm(instance=request.user)
    s=student.objects.filter(username=request.user.username)
    if s:
        context = {
        'delete_form': delete_form, 's':s[0]
    }
        return render(request, 'app/delete_account.html', context)
    context = {'delete_form': delete_form}
    return render(request, 'app/delete_account.html', context)


def home(request):

    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    stu = tutor.objects.all()
    s=student.objects.filter(username=request.user.username)
    if s:
        return render(
        request,
        'app/index.html',
       {'stu':stu,'s':s[0]})
    else:
         return render(
        request,
        'app/index.html',
       {'stu':stu})


def back(request):
    return home(request)

def show(request):

    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    stu = tutor.objects.all()

    print(request.POST.get('sts.name'))
    stu = tutor.objects.get(name="soso")

    stu = tutor.objects.get(name='Ayat')
    s=student.objects.filter(username=request.user.username)
    if s:
        return render(request,'app/show.html',{'stu':stu,'s':s[0]})
    return render(request,'app/show.html',{'stu':stu} )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    s=student.objects.filter(username=request.user.username)
    if s:
        return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,'s':s[0],
        }
    )
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
    s=student.objects.filter(username=request.user.username)
    if s:
        return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,'s':s[0],
        }
    )
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
            print(request.POST.getlist('coursees'))
            #form.coursees.add(request.POST.getlist('coursees'))
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


def prof(request):
    s=tutor.objects.filter(username=request.user.username)
    if s:
    #print(s[0].image)
        return render(request, 'app/profile.html',{'s':s[0]})
    s=student.objects.filter(username=request.user.username)
    return render(request, 'app/profilestud.html',{'s':s[0]})
  
def updatestud(request):
    s=student.objects.filter(username=request.user.username).update(color=request.POST.get("SEL"))
    
    
    s=student.objects.filter(username=request.user.username)
 
    return render(request, 'app/profilestud.html',{'s':s[0]}) 







class profile(UpdateView):
    model = tutor
    form = tutorChangeForm
    
    template_name = 'profile.html'
    #template_name = 'profile.html'


    #print(form.idt)
    fields = ['email','price','age','phone','idt','image']

    success_url = reverse_lazy('home') # This is where the user will be 
                                       # redirected once the form
                                       # is successfully filled in

    def get_object(self, **kwargs):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        return self.request.user
   
def sendtomanager(request):
    print(request.POST.get('sendmess'))
    #s=student.objects.filter(username=request.user.username)
    send_mail(
    'message from user '+request.user.username,
    request.POST.get('sendmess'),
    [request.user.email],
    ['safaaaz@ac.sce.ac.il'],
    fail_silently=True,
)
    return render(request, 'app/contact.html',{
            'title':'Contact',
            'message':'Your message has been sent to the administration',
            'year':datetime.now().year,
        }) 

def addchart(request,**kwargs):
    x=request.POST.getlist('course')
    s=student.objects.filter(username=request.user.username)
    print(tutor.objects.filter(id=request.POST.get('stuname')))
    print(s)
    if s.count()==0:
        print("noo")
    else:
        t=tutor.objects.filter(id=request.POST.get('stuname'))
        y=cart.objects.create(student=s[0],tutor=t[0],price=t[0].price)
        y.courses.create(name=request.POST.getlist('course'))
        
    # y.courses.set(request.POST.getlist('course'))
    #y.save()
    if s:
        return render(request, 'app/addchart.html',{'s':s[0]})
    return render(request, 'app/addchart.html')

def ourcart(request):
    s=student.objects.filter(username=request.user.username)
    stu = cart.objects.filter(student=s[0])
    if s:
        return render(request, 'app/ourcart.html',{'stu':stu,'s':s[0]})
    return render(request, 'app/ourcart.html',{'stu':stu})

def login_page(request):

    return render(request,'app/login_page.html')

def tutorstud(request):
    s=tutor.objects.filter(username=request.user.username)
    stu = cart.objects.filter(tutor=s[0])
    return render(request, 'app/showstud.html',{'stu':stu}) 

def CheckOut(request):
    s=tutor.objects.filter(username=request.user.username)
    if s:
        return render(request,'app/CheckOut.html',{'s':s[0]})
    return render(request,'app/CheckOut.html')





def showimage(request):

    lastimage= tutor.objects.last()

    image= lastimage.image


    form= ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'image': image,
              'form': form
              }
    
      
    return render(request, 'app/image.html', context)





import operator

from django.db.models import Q

def search_tutor(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            stu = tutor.objects.filter(name__contains=query_name)
            s=student.objects.filter(username=request.user.username)
            if s:
                return render( request, 'app/index.html',  {'stu':stu,'s':s[0]})
            return render( request, 'app/index.html',  {'stu':stu})


    return render(request, 'app/index.html')



    #return render(request,'app/CheckOut.html')

def Search(request):
    #query = request.GET.get('query')
    s=student.objects.filter(username=request.user.username)
    
    instock = request.GET.get('instock')
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 100000)
    sorting = request.GET.get('sorting', '-date_added')
    products = tutor.objects.filter().filter(price__gte=price_from).filter(price__lte=price_to)

    #if instock:
     #   products = products.filter(num_available__gte=1)
    if s:
        context = {
        #'query': query,
        'products': products.order_by(sorting),
        'instock': instock,
        'price_from': price_from,
        'price_to': price_to,
        'sorting': sorting, 's':s[0]
    }

        return render(request, 'app/Search.html',context)
    context = {
        #'query': query,
        'products': products.order_by(sorting),
        'instock': instock,
        'price_from': price_from,
        'price_to': price_to,
        'sorting': sorting,
    }
    
    return render(request, 'app/Search.html',context)





def product_list(request):
    
    f = ProductFilter(request.GET, queryset=tutor.objects.all())
    return render(request, 'app/template.html', {'filter': f})

def messagest(request):
    t=tutor.objects.filter(username=request.user.username)
    return render(request, 'app/messagest.html', {'totur': t[0]})

