from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User
from .forms import CustomUserCreationForm

# Create your views here.


def home(request):
    return render(request, "accounts/home.html")


def signin(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signin.html", context)


def index(request):
    user = User.objects.all()
    context = {
        "user": user,
    }
    return render(request, "accounts/index.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("home")


def detail(request, user_pk):
    user = User.objects.get(id=user_pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


def update(request, user_pk):
    return render(request, "accounts/update.html")
