from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Region)
admin.site.register(models.Department)
admin.site.register(models.TreePlan)
admin.site.register(models.TreeHeightReport)
