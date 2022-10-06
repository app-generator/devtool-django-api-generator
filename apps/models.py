from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=2020)
    