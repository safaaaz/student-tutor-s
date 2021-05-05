from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import tutorForm,studentForm,studentChangeForm,tutorChangeForm
from .models import student,tutor,course,cart


#class studentAdmin(UserAdmin):
#    add_form = studentForm
#    form = studentChangeForm
#    model = student
#    list_display = ['email', 'username']

admin.site.register(student)
admin.site.register(cart)

class UserProfileInline(admin.StackedInline):
    model = tutor
    filter_horizontal = ('coursees',)

class tutorAdmin(UserAdmin):

    model = tutor
    class Meta:
        verbose_name = 'tutor'
    list_display = ['username','is_ok','get_courses','field']
    search_fields=['price','name']
    list_editable = ('is_ok',)
    inlines = [UserProfileInline]

    def get_courses(self, obj):
        return "\n".join([p.name for p in obj.coursees.all()])
admin.site.register(tutor,tutorAdmin)

admin.site.register(course)

#class YourModelAdmin(admin.ModelAdmin):
   # pass

#admin.site.register(student, YourModelAdmin)