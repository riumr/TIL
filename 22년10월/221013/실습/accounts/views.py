from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.


def home(request):
    return render(request, "accounts/home.html")


def signin(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
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


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instace=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("home")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/password_change.html", context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("home")
