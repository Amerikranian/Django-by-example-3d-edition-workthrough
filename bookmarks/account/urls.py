from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Old and depricated login view
    # path("login/", views.user_login, name="login"),
    # Note: Default django authentication views expect their templates to be in templates/registration/
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.dashboard, name="dashboard"),
]
