from django.shortcuts import redirect,render,get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Count
from .models import MyDev,MyIdea
from .forms import RegisterForm

# Create your views here.
def idea_list(request):
    sort = request.GET.get('sort')
    ideas = MyIdea.objects.filter()

    if sort == 'latest':
        ideas = ideas.order_by('-id')
    elif sort == 'oldest':
        ideas = ideas.order_by('id')
    elif sort == 'name':
        ideas = ideas.order_by('title')
    elif sort == 'liked':
        ideas = ideas.filter(liked_by=request.user)

    return render(request, 'posts/idea_list.html',{'ideas': ideas})

def change_interest_rate(request, pk, rate):
    idea = get_object_or_404(MyIdea, pk=pk)
    idea.interest_rate = rate
    idea.save()
    return JsonResponse({'new_rate': idea.interest_rate})

def idea_detail(request, pk) :
     board_contents = get_object_or_404(MyIdea, pk = pk)
     print("board_contents", board_contents)
     return render(request, 'posts/idea_detail.html', {'board_contents' : board_contents})

def idea_register(request) :
    print('idea_register')
    if request.method == 'POST' :
          print('create_review_POST')
          form = RegisterForm(request.POST, request.FILES)
          if form.is_valid() :
               print('create_review_POST2')
               MyIdea = form.save()
               MyIdea.save()
               return redirect('/')

    idea_register_form = RegisterForm()
    return render(request, 'posts/idea_register.html', {'idea_register_form':idea_register_form})

def idea_like(request, pk):
    idea = get_object_or_404(MyIdea, pk=pk)
    user = request.user

    if user in idea.liked_by.all():
        # 이미 찜한 상태인 경우 찜 취소
        idea.liked_by.remove(user)
    else:
        # 찜하기
        idea.liked_by.add(user)

    return redirect('idea_detail', pk=pk)

def devtool_list(request):
    tools = MyDev.objects.filter()
    return render(request, 'posts/devtool_list.html', {'tools':tools})