from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):
    review = Review.objects.all()
    context = {'review': review, }
    return render(request, 'articles/index.html', context)


def new(request):
    context = {}
    return render(request, 'articles/new.html', context)


def edit(request, pk):
    review = Review.objects.get(pk=pk)
    context = {'review': review, }
    return render(request, 'articles/edit.html', context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {'review': review, }
    return render(request, 'articles/detail.html', context)


def create(request):
    title = request.GET.get('review_title')
    content = request.GET.get('content')
    created_at = request.GET.get('created_at')
    review = Review(title=title, content=content, created_at=created_at)
    review.save()
    return redirect('articles:index')


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('articles:index')


def update(request, pk):
    review = Review.objects.get(pk=pk)
    title = request.GET.get('review_title')
    content = request.GET.get('content')
    review.title = title
    review.content = content
    review.save()
    return redirect('articles:index')
