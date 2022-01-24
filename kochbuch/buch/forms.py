from django import forms

from django.contrib.auth.models import User
from .models import Profile, Comment


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','body')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }