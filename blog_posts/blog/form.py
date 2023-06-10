from django import forms
from .models import Comments, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text_comment',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tags', 'category', 'title', 'description']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user