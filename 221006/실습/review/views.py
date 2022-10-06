from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.


def index(request):
    movie = Movie.objects.all()
    context = {"movie": movie}
    return render(request, "reviews/index.html", context)


def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect("review:detail", movie.pk)
    else:
        form = MovieForm()
    context = {"form": form}
    return render(request, "reviews/create.html", context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect("review:index")


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie.save()
            return redirect("review:detail", movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {"movie": movie, "form": form}
    return render(request, "reviews/update.html", context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {"movie": movie}
    return render(request, "reviews/detail.html", context)
