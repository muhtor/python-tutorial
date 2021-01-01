from django.urls import path
from . import views

urlpatterns = [
    path('add', views.TreeHeightReportView.as_view(), name="add"),
]