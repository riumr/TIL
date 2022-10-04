from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    article = Article.objects.all()
    context = {'article': article}
    return render(request, 'article/index.html', context)


def new(request):
    context = {}
    return render(request, 'article/new.html', context)


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        article_form.save()
        redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {'article_form': article_form}
    return redirect('articles:index')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# 수정할 내용을 입력하는 템플릿


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article/edit.html', context)

# 수정 사항을 처리하는 함수


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return redirect("articles:index")
