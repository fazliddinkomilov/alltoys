from django.shortcuts import render

from toys.models import User, Toy



def show_users(request):
    users = User.objects.all()
    toys = Toy.objects.all()
    return render(request, 'toys/show_users.html', context={"users_list": users, "toys": toys})
