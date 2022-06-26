from validate_docbr import CPF
import re


def validate_cpf(numero_cpf):
    cpf = CPF()
    return cpf.validate_cpf(numero_cpf)

def validate_nome(nome):
    """Verifica se nome não contém numero"""
    return nome.isalpha()

def celular_valido(numero_celular):
    """Verifica se o numero do celular é valido DD XXXX-XXXX"""
    modelo = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    resposta = re.findall(modelo, numero_celular)
    return resposta
