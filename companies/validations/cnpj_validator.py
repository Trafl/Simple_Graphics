import re
from django.core.exceptions import ValidationError

def validate_cnpj(cnpj):

    cnpj = re.sub(r'\D', '', cnpj)


    if len(cnpj) != 14:
        raise ValidationError('O CNPJ deve ter 14 dígitos.')

    def calculate_digit(cnpj, weights):
        total = sum(int(cnpj[i]) * weights[i] for i in range(len(weights)))
        remainder = total % 11
        return '0' if remainder < 2 else str(11 - remainder)

    first_digit = calculate_digit(cnpj[:-2], [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    if first_digit != cnpj[12]:
        raise ValidationError('CNPJ inválido.')

    second_digit = calculate_digit(cnpj[:-1], [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    if second_digit != cnpj[13]:
        raise ValidationError('CNPJ inválido.')
