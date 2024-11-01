from django.db import models
from .validations.cnpj_validator import validate_cnpj

ESTADOS_BRASIL = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
)

class Companies(models.Model):

    name = models.CharField(verbose_name='Nome', max_length=250)
    cnpj = models.CharField( validators = [validate_cnpj], verbose_name= 'CNPJ', max_length=150)

    street = models.CharField(verbose_name='Rua', max_length=255)
    number = models.IntegerField(verbose_name= 'Numero')

    additional_info = models.CharField(verbose_name='Complemento', max_length=50, blank=True, null=True)
    neighborhood = models.CharField(verbose_name='Bairro', max_length=100)
    city = models.CharField(verbose_name='Cidade', max_length=100,)
    state = models.CharField(verbose_name='Estado', choices= ESTADOS_BRASIL, max_length=20)  
    zip_code = models.CharField(verbose_name='CEP', max_length=9)

    def __str__(self):
        return f"{self.name}, {self.cnpj}"


