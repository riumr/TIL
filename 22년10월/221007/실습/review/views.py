from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


# Create your views here.


def index(request):
    review = Review.objects.all()
    context = {"review": review}
    return render(request, "t_01/index.html", context)


def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect("review:index")
    else:
        form = ReviewForm()
    context = {"form": form}
    return render(request, "t_01/create.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {"review": review}
    return render(request, "t_01/detail.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect("review:detail", review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {"review": review, "form": form}
    return render(request, "t_01/update.html", context)


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect("review:index")
