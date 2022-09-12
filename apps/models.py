from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=2020)


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)

class City(models.Model):
    name = models.CharField(max_length=20)