from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

def post_list(request):
    posts = Post.published.all()
    return render(request, 'myblog/post/list.html', {'posts': posts})


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found")
    return render(request, 'myblog/post/detail.html', {'posts': posts})
    