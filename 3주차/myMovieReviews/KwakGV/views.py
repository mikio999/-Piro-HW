from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import myText
from .forms import ReviewForm

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

def login(request) :

    print("login")

    if request.method == 'POST' :

        print("login post")

        email = request.POST['email']
        pwd = request.POST['pwd']

        user = auth.authenticate(request, username=email, password=pwd)

        if user is None :
            print("회원가입된 사람이 아니겠죠?????")
            return redirect('/join')
        else :
            auth.login(request, user)
            return redirect('/')

    return render(request, 'KwakGV/login.html')


def join(request):

    print("join 실행!")
    if request.method == 'POST' :
        print("여기는 포스팅요청")

        email = request.POST['email']
        pwd = request.POST['pwd']

        User.objects.create_user(username=email, password=pwd)


        return redirect('/')

    print("join 마지막 부분")
    return render(request, 'KwakGV/join.html')

def logout(request) :

    auth.logout(request)

    return redirect('/')

def review_list_info(request, pk) :
     board_contents = get_object_or_404(myText, pk = pk)

     print(board_contents)

     return render(request, 'KwakGV/review_list_info.html', {'board_contents' : board_contents})

def create_review(request) : 
     print('create_review')
     if request.method == 'POST' :
          print('create_review_POST')
          form = ReviewForm(request.POST, request.FILES)
          if form.is_valid() :
               print('create_review_POST2')
               myText = form.save(commit=False)
               myText.author = request.user
               myText.save()
               return redirect('/')

     review_form = ReviewForm()
     return render(request, 'KwakGV/create_review.html', {'review_form':review_form})

def my_review(request) :
    reviews = myText.objects.filter(author=request.user)

    return render(request,'KwakGV/my_review.html', {'reviews':reviews})

def edit_review(request, pk):
     review = get_object_or_404(myText, pk=pk)

     if request.method == 'POST' :

        form = ReviewForm(request.POST,request.FILES, instance=review)

        if form.is_valid() :

            review = form.save(commit=False)
            review.author = request.user
            review.save()

            return redirect('review_list_info', pk=pk)

     else :

        form = ReviewForm(instance=review)

     return render(request, 'KwakGV/edit_review.html',
                  {'review_form': form,
                   'primary_key' : pk}
                  )

from django.shortcuts import get_object_or_404

def delete_review(request, pk):
    review = get_object_or_404(myText, pk=pk)

    if request.method == 'POST':
        review.delete()
        return redirect('/')  # 리뷰 삭제 후 리뷰 목록 페이지로 리디렉션

    return render(request, 'KwakGV/delete_review.html', {'review': review})
