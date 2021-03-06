from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Old and depricated login view
    # path("login/", views.user_login, name="login"),
    path("", views.dashboard, name="dashboard"),
    # Note: Default django authentication views expect their templates to be in templates/registration/
    # Full list of included urls is at https://github.com/django/django/blob/stable/3.0.x/django/contrib/auth/urls.py
    path("", include("django.contrib.auth.urls")),
    # social_django urlpatterns
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("register/", views.register, name="register"),
    # User profiles
    path("edit/", views.edit, name="edit"),
]
