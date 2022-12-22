from django.urls import path
from . import views

app_name = 'articles'  # 절대경로를 설정할 때 사용한다. url namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('update/<int:pk>', views.update, name='update'),
]
