from rest_framework import serializers
from . import models


class PersonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = '__all__'


class PersonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = '__all__'
