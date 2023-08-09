from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        exclude = ['author']
        widgets = {
            'body': CKEditorWidget()
        }