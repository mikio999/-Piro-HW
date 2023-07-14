from django.shortcuts import render,get_object_or_404
from .models import myText

# Create your views here.
def movie_list(request) :
    texts = myText.objects.filter()
    print(texts)
    return render(request, 'KwakGV/movie_list.html', {'texts':texts})

def review_list(request) :
     texts = myText.objects.filter()
     animation_movie = myText.objects.filter(genre="animation/drama")
     musical_movie = myText.objects.filter(genre="Romance/Musical")
     print(texts)
     return render(request, 'KwakGV/review_list.html', {'texts':texts, 'musical_movie': musical_movie, 'animation_movie': animation_movie})

def review_list_info(request, pk) :
     board_contents = get_object_or_404(myText, pk = pk)

     print(board_contents)

     return render(request, 'KwakGV/review_list_info.html', {'board_contents' : board_contents})