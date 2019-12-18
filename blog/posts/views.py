from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse

from posts.models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'posts/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    ordered_comments = post.comment_set.order_by('-pub_date')
    context = {
        'post': post,
        'ordered_comments': ordered_comments,
    }
    return render(request, 'posts/detail.html', context)


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.comment_set.create(text=request.POST['comment'])
    return HttpResponseRedirect(reverse('posts:detail', args=(post_id,)))
