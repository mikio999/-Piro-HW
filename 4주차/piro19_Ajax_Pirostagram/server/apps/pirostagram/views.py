from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from .models import MyReddit, Comment
from .forms import RegisterForm

# Create your views here.
@csrf_exempt
def index(request):
    reddits = MyReddit.objects.filter()

    reddit_comments = {}
    for reddit in reddits:
        comments = Comment.objects.filter(reddit=reddit)
        print('!!!!!!!!!!!!!!!!프린트문',comments)
        reddit_comments[reddit.id] = comments
        print('와와오아ㅗ아;왕 ㅗ레딧아이디!',reddit.id,reddit_comments[reddit.id])
        print('이제는 되었으면 좋겠어.', reddit_comments)

    return render (request, 'pirostagram/index.html', {'reddits':reddits, 'reddit_comments': reddit_comments})

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
            reddit = get_object_or_404(MyReddit, pk=reddit_id)
            comment = Comment.objects.create(reddit=reddit, comment=comment_text)
            return JsonResponse({'comment_id': comment.id})  # 댓글의 ID를 반환
        else:
            return JsonResponse({'error': 'Comment text is empty'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
        return JsonResponse({'message': '댓글이 성공적으로 삭제되었습니다.'})
    except Comment.DoesNotExist:
        return JsonResponse({'error': '댓글을 찾을 수 없습니다.'}, status=404)