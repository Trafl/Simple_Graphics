from django.shortcuts import render
from django.views.generic import DetailView
from .models import Companies

class CompanieDetailView(DetailView):
    model = Companies
    template_name = 'companie_admin.html'
    context_object_name = 'company'


