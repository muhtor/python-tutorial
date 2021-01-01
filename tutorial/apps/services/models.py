from django.db import models
from django.db.models import Sum

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    language = models.CharField(max_length=3)


class Post(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text[:10]


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.SmallIntegerField()

    def __str__(self):
        return f"{self.first_name}"



class Order(models.Model):
    subtotal = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return f"ID: {self.pk}"

    def calc(self):
        total = Order.objects.all().aggregate(total=Sum('total'))['total']
        # total = Order.objects.aggregate(Sum('total'))
        print("T....", total, type(total))

        return total