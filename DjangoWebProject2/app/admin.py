'''this model for admin site'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group,User


from app.models import student,tutor,course,cart,message,AboutMss,changeview

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(AboutMss)
admin.site.register(changeview)
admin.site.register(student)
admin.site.register(cart)


class UserProfileInline(admin.StackedInline):
    '''class for tutor profile'''
    model = tutor
    filter_horizontal = ('coursees','messages')

class TutorAdmin(UserAdmin):
    '''admin tutor class'''
    name='admin'
    model = tutor

    class Meta:
        '''class meta to get name'''
        def shatha(self):
            '''ss'''
            print(self)
        def safaa(self):
            '''soso'''
            print(self)

        verbose_name = 'tutor'
    list_display = ['username','is_ok','get_courses','field']
    search_fields=['price','name']
    list_editable = ('is_ok',)
    inlines = [UserProfileInline]

    def get_courses(self,obj):
        '''func to get courses'''
        print(self)
        return "\n".join([p.name for p in obj.coursees.all()])
admin.site.register(tutor,TutorAdmin)

admin.site.register(course)
admin.site.register(message)

#class YourModelAdmin(admin.ModelAdmin):
   # pass

#admin.site.register(student, YourModelAdmin)
