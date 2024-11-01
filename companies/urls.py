from django.urls import path
from . views import CompanieDetailView


urlpatterns = [

    path('companies/<int:pk>',CompanieDetailView.as_view(), name='companies_detail'),
]