from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()


class Toy(models.Model):
    name = models.CharField(max_length=100)


class Address(models.Model):
    address = models.CharField(max_length=100)


class Tag(models.Model):
    tag = models.CharField(max_length=10)
