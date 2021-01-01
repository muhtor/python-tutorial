from django.forms import ModelForm
from .models import Bird
from django.forms import modelformset_factory


class BirdForm(ModelForm):
    class Meta:
        model = Bird
        fields = ['common_name', 'scientific_name']


BirdFormSet = modelformset_factory(
    Bird, fields=("common_name", "scientific_name"), extra=1
)
