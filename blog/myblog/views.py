from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    sess = request.session.get('id', False)
    print(f'request: {request.user.is_authenticated}')
    if not request.session.get('id', False):
        raise PermissionDenied
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    if not request.session.get('id', False):
        raise PermissionDenied

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post':post})

def post_new(request):
    if not request.session.get('id', False):
        raise PermissionDenied

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'myblog/post_edit.html', {'form':form})

def post_edit(request, pk):
    if not request.session.get('id', False):
        raise PermissionDenied

    post = get_object_or_404(PostGuest, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myblog/post_edit.html', {'form':form})
