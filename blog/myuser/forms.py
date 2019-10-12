from django import forms
from .models import MyUser


class SignUpForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('username', 'password')
        #fields = ('username', 'password', 'registered_date')


class SignInForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('username', 'password')
        #fields = ('username', 'password', 'registered_date')
