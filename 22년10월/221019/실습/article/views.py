from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import ArticleForm
from .models import Article

# Create your views here.


def index(request):
    article = Article.objects.all()
    context = {
        "article": article,
    }
    return render(request, "articles/index.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/detail.html", context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("article:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)
