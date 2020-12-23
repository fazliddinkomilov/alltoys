from django.db import models


class ActiveObjectsManager(models.Model):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class User(models.Model):
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    active_object = ActiveObjectsManager()


class Toy(models.Model):
    name = models.CharField(max_length=100)


class Address(models.Model):
    address = models.CharField(max_length=100)


class Tag(models.Model):
    tag = models.CharField(max_length=10)
