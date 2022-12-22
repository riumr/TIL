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


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_Form = CommentForm()
    comments = article.comment_set.all()
    context = {
        "article": article,
        "commentForm": comment_Form,
        "comments": comments,
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


def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment_form.save()
    return redirect("article:detail", article.pk)


def comments_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("article:detail", pk)
