from django import forms
from .models import MyIdea

class RegisterForm(forms.ModelForm) :
    
    class Meta :
        model = MyIdea
        fields = (
            'title',
            'image',
            'content',
            'interest_rate',
            'devtool',
            'liked_by',
        )