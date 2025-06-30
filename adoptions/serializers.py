from rest_framework.serializers import ModelSerializer

from users.serializers import AdoptionUserSerializer
from .models import AdoptionPreference

# (1) 전체 데이터를 다 보여주는 Serialize
class AdoptionSerializer(ModelSerializer):
    user = AdoptionUserSerializer(read_only=True)

    class Meta:
        model = AdoptionPreference
        fields = "__all__"

from rest_framework import serializers
from .models import AdoptionMatch
from users.models import CustomUser
from cats.models import Cat
class SafeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','phone']


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'name', 'age', 'gender', 'breed']

class AdoptionMatchSerializer(serializers.ModelSerializer):
    user = SafeUserSerializer(read_only=True)  # 🔐 유저 정보 안전하게 보여주기
    cat = CatSerializer(read_only=True)
    class Meta:
        model = AdoptionMatch
        fields = ['id', 'user', 'cat', 'matched_at']
        depth = 1  # user, cat 객체의 내부 정보까지 보여줄 수 있음 (선택사항)

