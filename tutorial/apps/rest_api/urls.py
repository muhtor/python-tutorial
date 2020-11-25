from django.urls import path
from . import views


urlpatterns = [
    path('person/list', views.PersonListView.as_view(), name='list'),
    path('person/create', views.PersonAPIView.as_view(), name='create'),
    path('person/all', views.PersonsList.as_view(), name='all'),
    path('person/csv', views.PersonsCSV.as_view(), name='post'),
]