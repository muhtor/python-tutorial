from django.views.generic import ListView, TemplateView
from .models import Bird
from .forms import BirdFormSet
from django.urls import reverse_lazy
from django.shortcuts import redirect


class BirdListView(ListView):
    model = Bird
    template_name = "form/bird_list.html"


class BirdAddView(TemplateView):
    template_name = "form/add_bird.html"

    def get(self, *args, **kwargs):
        formset = BirdFormSet(queryset=Bird.objects.none())
        return self.render_to_response({'bird_formset': formset})

    # Define method to handle POST request
    def post(self, *args, **kwargs):
        formset = BirdFormSet(data=self.request.POST)
        # Check if submitted forms are valid
        if formset.is_valid():
            print("DATA...", formset.data)
            formset.save()
            return redirect(reverse_lazy("bird_list"))
        else:
            print("ERROR...", formset.errors)

        return self.render_to_response({'bird_formset': formset})
