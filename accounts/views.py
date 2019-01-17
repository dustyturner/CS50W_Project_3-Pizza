from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def auth_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("login", {"message": "Invalid login details"})
    if request.method == "GET":
        return render(request, "accounts/login.html", {"messgage": None})


def auth_register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username, email, password)

        login(request, user)

        return redirect("index")

    if request.method == "GET":
        return render(request, "accounts/register.html", {"messgage": None})


def auth_logout(request):
    logout(request)
    return redirect("menu")

