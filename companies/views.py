from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Companies
from .forms import CompanyForm

class CompanieDetailView(DetailView):
    model = Companies
    template_name = 'companie_detail.html'
    context_object_name = 'company'


class CompanieCreateView(CreateView):
    model = Companies
    template_name = 'companie_form.html'
    form_class = CompanyForm
#    success_url






