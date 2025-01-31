from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.sign_up, name="sign_up"),
    path("log-in/", views.log_in, name="log_in"),
    path("log-out/", views.log_out, name="log_out"),
    path("google/login/", views.google_login, name="google_login"),
    path("google/callback/", views.google_callback, name="google_callback"),
]
