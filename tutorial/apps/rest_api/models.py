from django.db import models
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=64)
    age = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.name}"
