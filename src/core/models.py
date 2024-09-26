# core/models.py
import os

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_media_file(file):
    # Allowed file extensions.
    allowed_exts = ["avi", "gif", "jpeg", "jpg", "mov", "mp4", "png"]  # Extensions
    ext = os.path.splitext(file.name)[1].lower().lstrip(".")
    if ext not in allowed_exts:
        raise ValidationError(
            f"Unsupported file extension: {ext}. Only followinf extensions are supported: {allowed_exts}."
        )


class Post(models.Model):
    # title = models.CharField(max_length=255)
    media_file = models.FileField(
        upload_to="media/", validators=[validate_media_file], blank=True, null=True
    )
    # caption = models.TextField()
    # content = models.TextField() # Create text field.

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f"{self.user.username} - {self.caption[:20]}..."
        return f"{self.user.username} - {self.media_file}..."


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}..."


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return f"{self.user.username} liked {self.post.content[:20]}..."
