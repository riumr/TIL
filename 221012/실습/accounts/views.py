from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from .models import User

# Create your views here.


def home(request):
    return render(request, "accounts/home.html")


def index(request):
    user = User.objects.all()
    context = {
        "user": user,
    }
    return render(request, "accounts/index.html", context)


def signup(request):
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
    return render(request, "accounts/signup.html", context)


def login(request):
    return render(request, "accounts/login.html")


def logout(request):
    return render(request, "accounts/logout.html")


def detail(request, user_pk):
    user = User.objects.get(id=user_pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)
