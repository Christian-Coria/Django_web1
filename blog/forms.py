from django import forms
from .models import Post

class PostCreateForms(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content')