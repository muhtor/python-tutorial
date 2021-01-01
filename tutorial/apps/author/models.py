from django.db import models


class Publishing(models.Model):
    name = models.CharField(max_length=64)


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub = models.ForeignKey(Publishing, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
