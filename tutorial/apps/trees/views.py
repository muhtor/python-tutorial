from django.views.generic import ListView, TemplateView
from .models import TreePlan, TreeHeightReport
from django.forms import (formset_factory, modelformset_factory)
from .forms import TreeHeightReportFirstForm, TreeHeightReportTwoForm
from django.urls import reverse_lazy
from django.views import View
from django.views import generic
from django.shortcuts import render, redirect
# Create your views here.


class TreeHeightReportView(View):
    template_name = 'trees/trees-report-add.html'

    def get(self, request):
        region_department = TreeHeightReportFirstForm()
        tree_report = TreeHeightReportTwoForm()
        ctx = {'region_department': region_department, 'tree_report': tree_report}
        return render(request, self.template_name, ctx)