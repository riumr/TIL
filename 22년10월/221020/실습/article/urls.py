from django.urls import path
from . import views

app_name = "article"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("<int:pk>/comments/", views.comments_create, name="comments_create"),
    path(
        "<int:pk>/comments/<int:comment_pk>/delete",
        views.comments_delete,
        name="comments_delete",
    ),
]
