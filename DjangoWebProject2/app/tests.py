"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from .models import *
from app.views import *
from app.forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact/')
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about/')
        self.assertContains(response, 'About', 3, 200)


    def test_login(self):
        """Tests the contact page."""
        self.client.login(username='soso', password='S263safa')
        response = self.client.get('/login/')
        self.assertContains(response, 'login', 4, 200)

    def test_show(self):
        response = self.client.get(reverse("show"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/show.html")
        

    


    def test_studentsignup(self):
        """Tests the about page."""
        response = self.client.get(reverse('studentsignup'))
        self.assertEquals(response.status_code, 200)
        


     
    def test_ssstudentsignup(self):
        """Tests the about page."""
        response = self.client.get(reverse('studentsignup'))
        self.assertTemplateUsed(response,"app/studentsignup.html")
    

    def test_checkout(self):
        response = self.client.get(reverse("CheckOut"))
        self.assertEquals(response.status_code, 200)
        

    def test_cccheckout(self):
        response = self.client.get(reverse("CheckOut"))
        self.assertTemplateUsed(response,"app/CheckOut.html") 


    def test_tutorstud(self):
        response = self.client.get(reverse("tutorstud"))
        self.assertEquals(response.status_code, 200)
        


    def test_tttutorstud(self):
        response = self.client.get(reverse("tutorstud"))
        self.assertTemplateUsed(response,"app/showstud.html")
        

  


    def test_ourcart(self):
        response = self.client.get(reverse("ourcart"))
        self.assertEquals(response.status_code, 200)
        


    def test_ooourcart(self):
        response = self.client.get(reverse("ourcart"))
        self.assertTemplateUsed(response,"app/ourcart.html")





  

    def test_deleteuser(self):
        self.client.login(username='soso', password='S263safa')
        response = self.client.get(reverse("deleteuser"))
        #self.assertEquals(response.status_code, 200)
        #self.assertTemplateUsed(response,"app/delete_account.html")
        self.assertEquals(response.status_code, 302)


 
       
    def test_signup_view(self):
        response = self.client.get(reverse("signup"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/signup.html")


    def test_sssignup_view(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response,"app/signup.html")

    def test_prof(self):
        response = self.client.get(reverse("profile"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/profilestud.html")



    def test_sendtomanager(self):
        response = self.client.get(reverse("sendtomanager"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/contact.html")


    def test_sssendtomanager(self):
        response = self.client.get(reverse("sendtomanager"))
        self.assertTemplateUsed(response,"app/contact.html") 

    def test_search_tutor(self):
        response = self.client.get(reverse("search"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/index.html")



    def test_sssearch_tutor(self):
        response = self.client.get(reverse("search"))
        self.assertTemplateUsed(response,"app/index.html") 




    def test_product_list(self):
        response = self.client.get(reverse("template"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/template.html")

    def test_ppproduct_list(self):
        response = self.client.get(reverse("template"))
        self.assertTemplateUsed(response,"app/template.html")

    def test_messagest(self):
        response = self.client.get(reverse("messagest"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/messagest.html")


    def test_mmmessagest(self):
        response = self.client.get(reverse("messagest"))
        self.assertTemplateUsed(response,"app/messagest.html") 

    def test_should_login_successfully(self):
        #user = self.create_test_user()
        response = self.client.post(reverse("login"), {
            'username': 'soso',
            'password': 'S263safa'
        })
        self.assertEquals(response.status_code, 200)

        #storage = get_messages(response.wsgi_request)

        #self.assertIn(f"Welcome {user.username}",
                      #list(map(lambda x: x.message, storage)))





class medelsTest(TestCase):
    def test_create_message(self):
        message1=message.objects.create(title="title for messs",content="this is content to test mess")
        message1.save()
        self.assertEqual(str(message1),"title for messs")

    def test_create_course(self):
        course1=course.objects.create(name="database")
        course1.save()
        self.assertEqual(str(course1),"database")

    def test_create_student(self):
        student1=student.objects.create(ids=555,name="safaa",age=7,phone=88)
        student1.save()
        self.assertEqual(str(student1),"safaa")

    def test_create_tutor(self):
        tutor1=tutor.objects.create(idt=555,name="safaa",age=7,phone=88,last_name="az")
        tutor1.save()
        self.assertEqual(str(tutor1),"safaa az")


class urlstest(SimpleTestCase):

    def test_about(self):
        url=reverse('about')
        self.assertEquals(resolve(url).func,about)

    def test_show(self):
        url=reverse('show')
        self.assertEquals(resolve(url).func,show)

    def test_template(self):
        url=reverse('template')
        self.assertEquals(resolve(url).func,product_list)

    def test_CheckOut(self):
        url=reverse('CheckOut')
        self.assertEquals(resolve(url).func,CheckOut)

    def test_Search(self):
        url=reverse('Search')
        self.assertEquals(resolve(url).func,home)

    def test_contact(self):
        url=reverse('contact')
        self.assertEquals(resolve(url).func,contact)

    def test_login(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,login)

    def test_sendtomanager(self):
        url=reverse('sendtomanager')
        self.assertEquals(resolve(url).func,sendtomanager)

    def test_signup(self):
        url=reverse('signup')
        self.assertEquals(resolve(url).func,signup_view)

    def test_search(self):
        url=reverse('search')
        self.assertEquals(resolve(url).func,search_tutor)

    def test_login_page(self):
        url=reverse('login_page')
        self.assertEquals(resolve(url).func,login_page)

    def test_addchart(self):
        url=reverse('addchart')
        self.assertEquals(resolve(url).func,addchart)

    def test_tutorstud(self):
        url=reverse('tutorstud')
        self.assertEquals(resolve(url).func,tutorstud)

    def test_messagest(self):
        url=reverse('messagest')
        self.assertEquals(resolve(url).func,messagest)

    def test_back(self):
        url=reverse('back')
        self.assertEquals(resolve(url).func,back)

    def test_ourcart(self):
        url=reverse('ourcart')
        self.assertEquals(resolve(url).func,ourcart)

    def test_studentsignup(self):
        url=reverse('studentsignup')
        self.assertEquals(resolve(url).func,studentsignup)

    def test_profile(self):
        url=reverse('profile')
        self.assertEquals(resolve(url).func,prof)

    def test_deleteuser(self):
        url=reverse('deleteuser')
        self.assertEquals(resolve(url).func,deleteuser)



class formstest(TestCase):

    #def test_tutorform_isok(self):
    #    form=tutorForm(data={
    #        'idt':444,
    #        'name':'safaa',
    #        'username':'sfsf7',
    #        'age':20,
    #        'price':40,
    #        'field':None,
    #        'image':None,
    #        'email':'safaa8721@gmail.com',
    #        'phone': 40 ,
    #        'coursees':None
    #        })

    #    self.assertTrue(form.is_valid())

    def test_tutorform_not_ok(self):
        form=tutorForm(data={})

        self.assertFalse(form.is_valid())

    def test_UserDeleteForm(self):
        form=UserDeleteForm(data={})

        self.assertTrue(form.is_valid())

    #def test_studentForm(self):
    #    form=studentForm({666 ,'yyy',
    #        'yyy',
    #        600,
    #        'fem',
    #        'safaa@gmail.com',
    #        674,
    #        None,})
    #    form.save()

    #    self.assertTrue(form.is_valid())

    def test_studentform_not_ok(self):
        form=tutorForm(data={})

        self.assertFalse(form.is_valid())

    def test_userForm_not_complite_fields(self):
        data = {
            'username': 'testuser',
            'email' : 'safaa8721@gmail.com',
        }

        form = UserCreationForm(data)
        
        self.assertFalse(form.is_valid())


class intgrationtest(TestCase):
    def test_show_tutor(self):
        response = self.client.get(reverse("show"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/show.html")

        response = self.client.get(reverse('studentsignup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/studentsignup.html")



    def test_deleteuser_login(self):
        self.client.login(username='soso', password='S263safa')
        response = self.client.get('/login/')
        self.assertContains(response, 'login', 4, 200)

        self.client.login(username='soso', password='S263safa')
        response = self.client.get(reverse("deleteuser"))
        self.assertEquals(response.status_code, 302)




    def test_search_tutor_prof(self):
        response = self.client.get(reverse("profile"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/profilestud.html")

        response = self.client.get(reverse("search"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/index.html")


    def test_ourcart_addchart(self):
         response = self.client.get(reverse("ourcart"))
         self.assertEquals(response.status_code, 200)
         self.assertTemplateUsed(response,"app/ourcart.html")

         response = self.client.get(reverse("addchart"))
         self.assertEquals(response.status_code, 200)
         self.assertTemplateUsed(response,"app/show.html")

    def test_sendtomanager_messagest(self):
        response = self.client.get(reverse("sendtomanager"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/contact.html")

        response = self.client.get(reverse("messagest"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"app/messagest.html")
        
    def test_create_tutor_tutor_stud_tutor_profile(self):
        tutor1=tutor.objects.create(idt=555,name="safaa",age=7,phone=88,last_name="az")
        tutor1.save()
        self.assertEqual(str(tutor1),"safaa az")

        url=reverse('tutorstud')
        self.assertEquals(resolve(url).func,tutorstud)

        url=reverse('profile')
        self.assertEquals(resolve(url).func,prof)















      