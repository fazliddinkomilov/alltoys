from django.db import models


class ActiveobjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class User(models.Model):
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    objects = models.Manager()

    active_objects = ActiveobjectsManager


class Toy(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name="toys", on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField( null=True, blank=True)


class Address(models.Model):
    address = models.CharField(max_length=100)


class Tag(models.Model):
    tag = models.CharField(max_length=10)
