from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Blog, User
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        exclude = ['author']
        widgets = {
            'body': CKEditorWidget()
        }
        
class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Create password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Confirm password'}),
    )
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name', 'autofocus': True}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
        }