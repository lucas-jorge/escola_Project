from rest_framework import serializers
from escola.models import Estudante,Curso

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'CPF', 'data_nascimento', 'numero_celular']
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'