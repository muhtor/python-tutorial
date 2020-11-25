from django.contrib import admin
from . import models
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'get_service', 'get_rank')


admin.site.register(models.Service)
admin.site.register(models.UserPersonalInfo, UserAdmin)
admin.site.register(models.UserServiceEvaluationRank)

