from django import forms
from .models import TreePlan, TreeHeightReport
from django.forms import modelformset_factory


class TreeHeightReportFirstForm(forms.ModelForm):
    
    class Meta:
        model = TreeHeightReport
        fields = ('region', 'department',)
        exclude = (
            'tree_plan',
            'height_0_0_2_count',
            'height_0_2_5_count',
            'height_0_5_1_count',
            'height_1_1_5_count',
            'height_1_5_2_count',
            'date',
        )


class TreeHeightReportTwoForm(forms.ModelForm):
    class Meta:
        model = TreeHeightReport
        fields = (
            'tree_plan',
            'height_0_0_2_count',
            'height_0_2_5_count',
            'height_0_5_1_count',
            'height_1_1_5_count',
            'height_1_5_2_count',
            'date',
        )
        exclude = ('region', 'department')
