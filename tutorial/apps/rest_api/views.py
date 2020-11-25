from django.http import HttpResponse
from . import models
from . import serializers
from django.shortcuts import render
from django.views import View
import csv
import io
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from . models import Person
# Create your views here.


class PersonAPIView(APIView):
    """http://127.0.0.1:8000/api/person/create"""
    def post(self, request):
        serializer = serializers.PersonCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PersonListView(generics.ListAPIView):

    serializer_class = serializers.PersonListSerializer

    def get_queryset(self):
        return models.Person.objects.all()


class PersonsList(View):
    """http://127.0.0.1:8000/api/person/all"""
    template_name = "person.html"

    def get(self, request, *args, **kwargs):
        try:
            person = Person.objects.all()
            context = {"persons": person}
            return render(request, self.template_name, context)
        except Exception as e:
            exception_context = {"exception": e.args}
            return render(request, self.template_name, exception_context)


class PersonsCSV(View):
    """http://127.0.0.1:8000/api/person/all"""
    template_name = "person.html"

    def post(self, request, *args, **kwargs):
        qs = Person.objects.all()
        if qs.exists():
            return self.create_csv(table=qs)
        else:
            exception_context = {"exception": "Object does not exists"}
            return render(request, self.template_name, exception_context)

    def create_csv(self, table):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="person.csv"'
        writer = csv.writer(response)
        opts = table.model._meta
        field_names = [field.name for field in opts.fields]
        writer.writerow(field_names)
        for obj in table:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response