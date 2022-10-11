from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "accounts/index.html")


def create(request):
    return render(request, "accounts/signup.html")


def detail(request):
    return render(request, "accounts/detail.html")
