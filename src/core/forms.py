# core/forms.py

from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # TODO: Add title and caption to media file.
        # fields = ["title", "caption", "media_file"]
        fields = ["media_file"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
