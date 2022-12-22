from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.


def index(request):
    article = Article.objects.all()
    context = {'article': article}
    return render(request, 'article/index.html', context)


def new(request):
    return render(request, 'article/new.html')


def create(request):
    article_form = ArticleForm(request.GET)
    article_form.save()
    return redirect('articles:index')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    title = request.GET.get('title')
    content = request.GET.get('content')
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:index')
