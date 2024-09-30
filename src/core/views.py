from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comment, Like
from .forms import CommentForm, PostForm
from .services import PostService


# Signup view.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("feed")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


# Login view.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("feed")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


# Logout view.
@login_required
def logout_view(request):
    logout(request)
    return redirect("feed")


# View for logged in user feed and public feed.
def feed(request):
    # Fetch all media files.
    posts = PostService.get_all_feed()
    return render(request, "feed.html", {"posts": posts})


# View for creating a post.
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("feed")
    else:
        form = PostForm()
    return render(request, "post_create.html", {"form": form})


# View for deleting a post.
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    post.delete()
    return redirect("feed")


# View for commenting on a post.
@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("feed")
    else:
        form = CommentForm()
    return render(request, "comment_create.html", {"form": form, "post": post})


# View for deleting a comment.
@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    comment.delete()
    return redirect("feed")


# View for liking a post.
@login_required
def like(request, pk):
    like_count = PostService.get_like_count(request.user, pk)
    return redirect("feed")


# View for showing a user's profile.
def user_profile(request, username):
    context = PostService(username)
    return render(request, "user_profile.html", context)
