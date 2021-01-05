from django.db import models


class Company(models.Model):
    salary = models.IntegerField() + '$'


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    destination = models.CharField(max_length=50)
