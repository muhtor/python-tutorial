from django.urls import path
from . import views

urlpatterns = [
    path('data', views.ParserView.as_view(), name='parser'),
    path('price', views.PriceView.as_view(), name='price'),
    path('separator', views.Separator.as_view(), name='separator'),
]
