from django.urls import path
from . import views


urlpatterns = [
    path('paycom/', views.TestView.as_view()),
    path('invoce', views.CreateInvoiceView.as_view(), name='create'),
]
