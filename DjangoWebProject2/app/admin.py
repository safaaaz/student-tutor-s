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

class tutorAdmin(UserAdmin):

    model = tutor
    class Meta:
        verbose_name = 'tutor'
    list_display = ['username','is_ok']
    search_fields=['price','name']
admin.site.register(tutor,tutorAdmin)


#class YourModelAdmin(admin.ModelAdmin):
   # pass

#admin.site.register(student, YourModelAdmin)