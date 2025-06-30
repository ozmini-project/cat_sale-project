from urllib import request

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import AdoptionMatch,AdoptionPreference
from .serializers import AdoptionSerializer, AdoptionMatchSerializer
from rest_framework.response import Response
from rest_framework import status

from .services import matching_for_user


class ListView(APIView):
    def get(self, request):
        adoptions_lists = AdoptionPreference.objects.all()
        serializer = AdoptionSerializer(adoptions_lists, many=True)
        return Response(serializer.data)

class CreateView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "로그인한 사용자만 가능합니다."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # 유저당 입양 조건이 이미 있으면 생성 불가
        if AdoptionPreference.objects.filter(user=request.user).exists():
            return Response(
                {"detail": "입양 조건은 한 개만 생성할 수 있습니다. 기존 조건을 수정하세요."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = AdoptionSerializer(data=request.data)
        if serializer.is_valid():
            adoptions = serializer.save(user=request.user)
            serializer = AdoptionSerializer(adoptions)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)


class DetailView(APIView):
    def put(self, request, adoption_id):
        preference = get_object_or_404(AdoptionPreference, id=adoption_id)

        # 본인 조건인지 확인 (다른 사람이 수정 못 하도록)
        if preference.user != request.user:
            return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

        serializer = AdoptionSerializer(preference, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, adoption_id):
        preference = get_object_or_404(AdoptionPreference, id=adoption_id)

        if preference.user != request.user:
            return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

        preference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RunMatchingView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)

        matches = matching_for_user(request.user)
        serializer = AdoptionMatchSerializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MatchesList(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)

        matches = AdoptionMatch.objects.filter(user=request.user)
        serializer = AdoptionMatchSerializer(matches, many=True)
        return Response(serializer.data)