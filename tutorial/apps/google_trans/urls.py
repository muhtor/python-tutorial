from django.urls import path
from . import views


urlpatterns = [
    path('translate', views.GoogleTranslateApiView.as_view(), name='trans'),
]