from django.contrib import admin
from .models import Companies


@admin.register(Companies)
class CompanieAdmin(admin.ModelAdmin):
    list_display =('name', 'cnpj')
    search_fields = ('name',)