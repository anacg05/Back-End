# serializers transforma a tabela em json

from rest_framework import serializers
from .models import Autor

class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
