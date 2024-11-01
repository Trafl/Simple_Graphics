from django import forms
from . models import Companies

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['name', 'cnpj', 'street', 'number', 'additional_info', 'neighborhood', 'city', 'state', 'zip_code']

