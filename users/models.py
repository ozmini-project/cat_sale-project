from django.contrib.auth.models import AbstractUser  # Django 기본 사용자 기능을 제공하는 추상 클래스
from django.db import models  # 모델을 만들기 위한 Django ORM 모듈

class CustomUser(AbstractUser):  # Django의 기본 사용자 모델을 확장하여 커스텀 사용자 모델 정의
    phone = models.CharField(max_length=20, blank=True)  # 전화번호 필드, 비워도 됨
    is_shelter = models.BooleanField(default=False)  # 보호소 여부 체크 (True면 보호소 계정)

    def __str__(self):
        return self.username  # 관리자 페이지나 출력할 때 사용자 이름을 보여줌
