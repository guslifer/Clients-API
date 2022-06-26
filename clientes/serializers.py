from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not validate_cpf(data["cpf"]):
            raise serializers.ValidationError({"cpf": "Esse cpf é inválido em, mano"})

        if not validate_nome(data["nome"]):
            raise serializers.ValidationError({"nome": "Vix, não pode ter numero..."})

        if not celular_valido(data["celular"]):
            raise serializers.ValidationError({"celular": "Formato inválido. Ex: 11 91234-1234"})
        return data

    