from django.shortcuts import render

from alltoys.toys.models import User, Toy


def show_users(request):
    users = User.objects.all()
    toys = Toy.objects.all()
    return render(request, "toys\show_users.html", context={"users": users, "toys": toys})
