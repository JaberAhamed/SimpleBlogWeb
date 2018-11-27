from django import forms
from .models import articla,author,comment,catagory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class creatForm(forms.ModelForm):

    class Meta:
        model = articla
        fields = [

            'title',
            'body',
            'image',
            'catagory',
        ]

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
 ]

class authorForm(forms.ModelForm):
    class Meta:
        model = author
        fields = [
            'image',
            'details',
 ]

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = [
            'name',
            'email',
            'post_comment',

        ]

class createCatagory(forms.ModelForm):
    class Meta:
        model = catagory
        fields = [
            'name',

        ]








