"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


from .models import tutor,student

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class tutorForm(UserCreationForm):
    class Meta:
        model = tutor
        fields = ['idt','name','username','age','price','field','image','email','phone','courses',]

class tutorChangeForm(UserChangeForm):
    class Meta:
        model = tutor
        fields = ['idt','name','username','password','age','price','field','image','email','phone','courses']

class studentForm(UserCreationForm):
    class Meta:
        model = student
        fields = ['ids','name','username','age','gender','email','phone','pic',]

class studentChangeForm(UserChangeForm):
    class Meta:
        model = student
        fields = ['ids','name','password','age','gender','email','phone','pic']
