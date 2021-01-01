from django.urls import path
from . import views

urlpatterns = [
    path('', views.BirdListView.as_view(), name="bird_list"),
    path('add', views.BirdAddView.as_view(), name="add_bird"),

]
