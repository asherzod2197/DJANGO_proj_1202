from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }

    return render(request, 'index.html', context=context)

def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )

    context = {
        'post' : post,
    }

    return render(request, 'post_detail', context=context)