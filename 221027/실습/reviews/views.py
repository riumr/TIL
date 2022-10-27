from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommnetForm

# Create your views here.


def index(request):
    review = Review.objects.all()
    context = {
        "review": review,
    }
    return render(request, "reviews/index.html", context)


def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reviews:index")
    else:
        form = ReviewForm()
        context = {
            "form": form,
        }
    return render(request, "reviews/create.html", context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


def comment_create(request, review_pk):
    comment_form = CommnetForm(request.POST)
    context = {
        "comment_form": comment_form,
    }
    return redirect("reviews:detail", review_pk)
