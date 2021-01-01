from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Post)
admin.site.register(models.Person)


class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'subtotal', 'total', 'calc')


admin.site.register(models.Order, OrderAdmin)
