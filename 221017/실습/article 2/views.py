from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


def index(request):
    article = Article.objects.all()
    context = {
        "article": article,
    }
    return render(request, "articles/index.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = ArticleForm(instance=article)
    context = {"form": form, "article": article}
    return render(request, "articles/update.html", context)
