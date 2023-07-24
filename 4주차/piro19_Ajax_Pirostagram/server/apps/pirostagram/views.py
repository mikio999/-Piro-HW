from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .models import MyReddit

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