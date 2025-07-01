from rest_framework import serializers
from .models import Cat

class CatSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Cat
        fields = '__all__'
