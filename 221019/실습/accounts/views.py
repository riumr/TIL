from django.shortcuts import render
from article.models import Article

# Create your views here.


def profile(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, "accounts/profile.html")
