from django import forms
from .models import Post, CustomUser
from django.contrib.auth.forms import PasswordChangeForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']



class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label="Старый пароль")
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="Новый пароль")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Повторите новый пароль")