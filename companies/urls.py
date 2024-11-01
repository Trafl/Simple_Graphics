from django.urls import path
from . views import CompanieDetailView, CompanieCreateView


urlpatterns = [

    path('companies/<int:pk>',CompanieDetailView.as_view(), name='companies_detail'),
    path('companies/register',CompanieCreateView.as_view(), name='companies_create'),
]