from django.contrib import admin
from .models import UserServiceEvaluation, UserInfo
from django.db import models
from django.forms import Textarea, TextInput


class UserInfoAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'gender', 'room', 'phone', 'date_created')
    search_fields = ('full_name', 'room', 'phone')
    # readonly_fields = ('full_name', 'gender', 'room', 'phone', 'date_created')
    filter_horizontal = ()
    list_filter = ('gender', 'date_created')
    fieldsets = ()
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_per_page = 50


class UserServiceEvaluationAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_1', 'service_2', 'service_3', 'service_4', 'feedback', 'date_created')
    search_fields = ('user', )
    # readonly_fields = ('service1_rank', 'service2_rank', 'service3_rank', 'service4_rank', 'feedback', 'date_created')
    filter_horizontal = ()
    list_filter = ('date_created', 'service1_rank', 'service2_rank', 'service3_rank', 'service4_rank')
    fieldsets = ()
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '80'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 80})},
    }
    list_per_page = 50


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserServiceEvaluation, UserServiceEvaluationAdmin)

admin.site.site_header = 'Wellmore Resort Hotel-Charvak'

