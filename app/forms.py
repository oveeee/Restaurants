from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField, PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation


class RegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Conform Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.
                              EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email': 'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs=
                {'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs=
                {'autocomplete':'current-password', 'class':'form-control'}))
    
class SendEmail(PasswordResetForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

class ConfirmPassword(SetPasswordForm):
    new_password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label='Conform Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 