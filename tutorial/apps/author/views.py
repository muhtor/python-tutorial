from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Author, Book, Publishing
from django.views import View
from django.views import generic
# Create your views here.


class CreateView(View):

    def get(self, request):
        template_name = 'author/book.html'
        book_inline_formset = inlineformset_factory(Author, Book, Publishing, fk_name=('name',), fields=('__all__',))
        formset = book_inline_formset()
        return render(request, template_name, {'formset': formset})
        pass

    def post(self, request):
        book_inline_formset = inlineformset_factory(Author, Book, Publishing, fields=('title',))
        formset = book_inline_formset(request.POST)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return redirect('/')
        else:
            return redirect('/')

