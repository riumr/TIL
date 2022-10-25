from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.index, name="index"),
    path("profile/<username>", views.profile, name="profile"),
    path("<int:pk>/follow", views.follow, name="follow"),
]
