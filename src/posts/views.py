from django.shortcuts import render
from .models import Post


def list_posts(request):
    # 이 메소드가 추가한 코드
    posts = Post.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, "posts/post_list.html", context)
