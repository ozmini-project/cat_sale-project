from rest_framework.serializers import ModelSerializer
from .models import CustomUser

# Feed에서 노출시킬 User Serializer
class AdoptionUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser

        fields = ("username", "phone")