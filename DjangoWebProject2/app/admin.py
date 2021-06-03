from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group,User


from .forms import tutorForm,studentForm,studentChangeForm,tutorChangeForm
from .models import student,tutor,course,cart,message,AboutMss


#class studentAdmin(UserAdmin):
#    add_form = studentForm
#    form = studentChangeForm
#    model = student
#    list_display = ['email', 'username']
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(AboutMss)

admin.site.register(student)
admin.site.register(cart)
#admin.site.register(messages)

class UserProfileInline(admin.StackedInline):
    model = tutor
    filter_horizontal = ('coursees','messages')

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
admin.site.register(message)

#class YourModelAdmin(admin.ModelAdmin):
   # pass

#admin.site.register(student, YourModelAdmin)