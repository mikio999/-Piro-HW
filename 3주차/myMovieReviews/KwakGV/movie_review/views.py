from django.shortcuts import render
from .models import myText

# Create your views here.
def movie_list(request) :
    texts = myText.objects.filter()
    return render(request, 'movie_review/movie_list.html', {'texts':texts})