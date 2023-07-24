from django import forms
from .models import MyReddit, Comment

class RegisterForm(forms.ModelForm) :
    class Meta:
        model = MyReddit
        fields = (
            '__all__'
        )

class CommentForm(forms.ModelForm) :
    class Meta:
        model = Comment
        fields = (
            '__all__'
        )