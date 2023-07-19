from django.shortcuts import redirect,render,get_object_or_404
from django.core.paginator import Paginator
from .models import MyDev,MyIdea

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
     print(board_contents)
     return render(request, 'posts/idea_detail.com', {'board_contents' : board_contents})

# def idea_register(request) :
#     print('idea_register')
#      if request.method == 'POST' :
#           print('create_review_POST')
#           form = ReviewForm(request.POST, request.FILES)
#           if form.is_valid() :
#                print('create_review_POST2')
#                myText = form.save(commit=False)
#                myText.save()
#                return redirect('/')

#      review_form = ReviewForm()
#      return render(request, 'KwakGV/create_review.html', {'review_form':review_form})

def devtool_list(request):
    tools = MyDev.objects.filter()
    return render(request, 'posts/devtool_list.html', {'tools':tools})