from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import tutorForm,studentForm,studentChangeForm
from .models import student,tutor


#class studentAdmin(UserAdmin):
#    add_form = studentForm
#    form = studentChangeForm
#    model = student
#    list_display = ['email', 'username']

admin.site.register(student)

#class tutorAdmin(UserAdmin):
#    add_form = tutorForm
#    form = tutorChangeForm
 
#    model = tutor
#    class Meta:
#        verbose_name = 'Edited Address'
#        verbose_name_plural = 'Edited Addresses'
#    list_display = ['email', 'username']
#    search_fields=['price','name']
admin.site.register(tutor)


#class YourModelAdmin(admin.ModelAdmin):
   # pass

#admin.site.register(student, YourModelAdmin)