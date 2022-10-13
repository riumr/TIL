from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", views.signin, name="signin"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("int:<user_pk>/", views.detail, name="detail"),
    path("update/", views.update, name="update"),
    path("password/", views.password_change, name="password_change"),
    path("delete/", views.delete, name="delete"),
]
