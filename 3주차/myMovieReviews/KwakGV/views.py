from django.shortcuts import render
from .models import myText

# Create your views here.
def movie_list(request) :
    texts = myText.objects.filter()
    print(texts)
    return render(request, 'KwakGV/movie_list.html', {'texts':texts})