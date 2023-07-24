from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from .models import MyReddit, Comment
from .forms import RegisterForm

# Create your views here.
@csrf_exempt
def index(request):
    reddits = MyReddit.objects.filter()

    return render (request, 'pirostagram/index.html', {'reddits':reddits})

def change_like_rate(request,pk,rate):
    reddit = get_object_or_404(MyReddit, pk=pk)
    reddit.like_rate = rate
    reddit.save()
    return JsonResponse({'new_rate': reddit.like_rate})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            my_reddit = form.save(commit=False)
            my_reddit.save()
            return redirect('/')
    else:
        form =RegisterForm()
    return render(request, 'pirostagram/register.html', {'reddit_register_form': form})

def submit_comment(request, reddit_id):
    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        if comment_text:
            reddit = MyReddit.objects.get(pk=reddit_id)
            comment = Comment.objects.create(reddit=reddit, text=comment_text)
            return JsonResponse({'comment_text': comment.text})
    return JsonResponse({'error': 'Invalid request'})