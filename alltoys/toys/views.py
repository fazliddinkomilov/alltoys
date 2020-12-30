from django.shortcuts import render

from toys.models import User, Toy


def show_users(request):
    users = User.objects.all()
    return render(request, 'toys/show_users.html', context={"users": users})


def dashboard(request):
    return render(request, "toys/dashboard.html", context={"Welcome_text": "Welcome to all_toys,  fazliddinkomilov"})


def show_toys(request):
    toys = Toy.objects.all()
    return render(request, 'toys/show_users.html', context={"toys": toys})