from django.urls import path
from . import views

app_name = 'wellmax'

urlpatterns = [
    path('user/profile', views.user_info_view, name='profile'),
    path('user/evaluation/<token>', views.user_evaluation_view, name='evaluation')
]