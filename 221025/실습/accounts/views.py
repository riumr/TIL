from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

# Create your views here.


def profile(request, username):
    user = get_user_model()
    person = user.objects.get(username=username)
    context = {
        "person": person,
    }
    return render(request, "accounts/profile.html", context)


def follow(request, pk):
    user = get_user_model()
    person = get_user_model().objects.get(pk=pk)
    person.followers.add(request.user)
    return redirect("accounts:profile", person.username)


def index(request):
    return render(request, "accounts/index.html")
