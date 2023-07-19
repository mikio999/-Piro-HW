from django.shortcuts import redirect,render,get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import MyDev,MyIdea
from .forms import RegisterForm, ToolForm

# Create your views here.
def idea_list(request):
    sort = request.GET.get('sort')
    ideas = MyIdea.objects.all()

    if sort == 'latest':
        ideas = ideas.order_by('-id')
    elif sort == 'oldest':
        ideas = ideas.order_by('id')
    elif sort == 'name':
        ideas = ideas.order_by('title')
    elif sort == 'liked':
        ideas = ideas.filter(liked_by=request.user)

    paginator = Paginator(ideas, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/idea_list.html', {'page_obj': page_obj})


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
          print('idea_register_POST')
          form = RegisterForm(request.POST, request.FILES)
          if form.is_valid() :
               print('idea_register_POST2')
               MyIdea = form.save()
               MyIdea.save()
               return redirect('/')

    idea_register_form = RegisterForm()
    return render(request, 'posts/idea_register.html', {'idea_register_form':idea_register_form})

def idea_like(request, pk):
    idea = get_object_or_404(MyIdea, pk=pk)
    user = request.user

    if user in idea.liked_by.all():
        idea.liked_by.remove(user)
    else:
        idea.liked_by.add(user)

    return redirect('posts:idea_detail', pk=pk)

def idea_modify(request, pk):
    if request.method == 'GET':
        post = MyIdea.objects.get(id=pk)
        form = RegisterForm(instance=post)    
        ctx = {'form': form,          
            'pk': pk}  
    
        return render(request, 'posts/idea_modify.html', context=ctx)
    else:
        post = MyIdea.objects.get(id=pk)
        form = RegisterForm(request.POST, request.FILES, instance=post)
        if form.is_valid():      
            form.save()
        
        return redirect('posts:idea_detail', pk=pk)

def idea_delete(request, pk):
    idea = MyIdea.objects.get(id=pk)
    idea.delete()
    return redirect('/')


def devtool_list(request):
    tools = MyDev.objects.filter()
    return render(request, 'posts/devtool_list.html', {'tools':tools})

def devtool_register(request) :
    devtool_register_form = ToolForm()
    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES)
        if form.is_valid():
            my_dev_tool = form.save(commit=False)
            my_dev_tool.save()
            return redirect('/devtool_list/')
    else:
        devtool_register_form = ToolForm()
        return render(request, 'posts/devtool_register.html', {'devtool_register_form':devtool_register_form})
    

def devtool_detail(request, pk):
    board_contents = get_object_or_404(MyDev, pk=pk)
    ideas = MyIdea.objects.filter(devtool=board_contents)
    print(ideas)
    return render(request, 'posts/devtool_detail.html', {'board_contents': board_contents, 'ideas': ideas})


def devtool_modify(request, pk):
    post = get_object_or_404(MyDev, pk=pk)

    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:devtool_detail', pk=pk)
    else:
        form = ToolForm(instance=post)
    
    ctx = {'form': form, 'pk': pk}
    return render(request, 'posts/devtool_modify.html', context=ctx)


    
def devtool_delete(request, pk):
    tool = MyDev.objects.get(id=pk)
    tool.delete()
    return redirect('/devtool_list/')