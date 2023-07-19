from django.shortcuts import redirect,render,get_object_or_404
from django.core.paginator import Paginator
from .models import MyDev,MyIdea
from .forms import RegisterForm

# Create your views here.
def idea_list(request):
    ideas = MyIdea.objects.filter()
    # paginator = Paginator(ideas, 4)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # return render(request, 'posts/idea_list.html',{'ideas': ideas}, {'page_obj': page_obj})
    return render(request, 'posts/idea_list.html',{'ideas': ideas})

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
               MyIdea = form.save(commit=False)
               MyIdea.save()
               return redirect('/')

    idea_register_form = RegisterForm()
    return render(request, 'posts/idea_register.html', {'idea_register_form':idea_register_form})

def devtool_list(request):
    tools = MyDev.objects.filter()
    return render(request, 'posts/devtool_list.html', {'tools':tools})