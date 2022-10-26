from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.


def index(request):
    article = Article.objects.all()
    context = {
        "article": article,
    }
    return render(request, "article/index.html", context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comment = article.comment_set.all()
    context = {
        "article": article,
        "comment_form": comment_form,
        "comment": comment,
    }
    return render(request, "article/detail.html", context)


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
    return render(request, "article/create.html", context)


def comment_create(request, article_pk):
    comment_form = CommentForm(request.POST)
    article = Article.objects.get(pk=article_pk)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    comment_form.save()
    return redirect("article:detail", article.pk)


def comment_delete(request, article_pk, comment_pk):
    return redirect("artile:detail", article.article_pk, comment.comment_pk)
