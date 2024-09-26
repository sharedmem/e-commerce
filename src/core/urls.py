# core/urls.py
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, re_path

from . import views


def redirect_to_feed(request):
    return redirect("feed")


urlpatterns = [
    # Home page.
    # path('', views.home, name='default'),
    # Redirecting to Home Page to Feed Page.
    path("", redirect_to_feed),
    # Signup Page.
    path("signup/", views.signup, name="signup"),
    # Login.
    path("login/", views.login_view, name="login"),
    # Logout.
    path("logout/", views.logout_view, name="logout"),
    # Feed Page.
    path("feed/", views.feed, name="feed"),
    # Post Create.
    path("post/create/", views.post_create, name="post_create"),
    # Post Delete.
    path("post/<int:pk>/delete/", views.post_delete, name="post_delete"),
    # Comment on Posts.
    path("post/<int:pk>/comment/", views.comment_create, name="comment_create"),
    # Delete Comment.
    path("comment/<int:pk>/delete/", views.comment_delete, name="comment_delete"),
    # Like Post.
    path("post/<int:pk>/like/", views.like, name="like"),
    # User's profile.
    path("profile/<username>", views.user_profile, name="user_profile"),
    # Admin's page.
    path("admin/", admin.site.urls),
]
