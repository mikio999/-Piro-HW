from django import forms
from .models import MyIdea, MyDev

class RegisterForm(forms.ModelForm) :
    
    class Meta :
        model = MyIdea
        fields = (
            'title',
            'image',
            'content',
            'interest_rate',
            'devtool',
        )

class ToolForm(forms.ModelForm) :

    class Meta :
        model = MyDev
        fields = (
            '__all__'
        )