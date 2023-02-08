from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

from django.contrib.auth import get_user_model
User = get_user_model()


# 추가

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    name = forms.CharField(label="이름")
    phone = forms.CharField(label="전화번호")
    address = forms.CharField(label="주소")

    class Meta(UserCreationForm):

        model = User
        fields = ("username", "password1", "password2", "email", "name", "phone", "address")

#mypage userform
class UpdateUserForm(forms.ModelForm):
    #username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=13, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ("email", "name", "phone", "address")


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))


    class Meta:
        model = Profile
        fields = ['avatar']