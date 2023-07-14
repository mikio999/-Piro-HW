from django import forms
from .models import myText

class ReviewForm(forms.ModelForm) :
    
    class Meta :
        model = myText
        fields = (
            'title',
            'year',
            'genre',
            'star_rate',
            'img_url',
            'actor',
            'director',
            'running_time',
            'board_text',

        )
