from django.db import models  # Django 모델 모듈
from django.conf import settings  # AUTH_USER_MODEL을 사용하기 위해
from cats.models import Cat  # 고양이 모델을 가져옴

class AdoptionPreference(models.Model):  # 입양을 원하는 조건을 저장하는 모델
    GENDER_CHOICES = [  # 원하는 성별 선택지
        ('M', 'Male'),
        ('F', 'Female'),
        ('A', 'Any'),  # 어떤 성별이든 상관없음
    ]

    user = models.ForeignKey(  # 조건을 등록한 사용자
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='preferences'  # user.preferences로 접근 가능
    )
    preferred_breed = models.CharField(max_length=50, blank=True)  # 원하는 품종 (비워도 됨)
    preferred_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='A')  # 성별 선호
    age_min = models.PositiveIntegerField(default=0)  # 원하는 최소 나이
    age_max = models.PositiveIntegerField(default=30)  # 원하는 최대 나이
    created_at = models.DateTimeField(auto_now_add=True)  # 등록 시간 저장

    def __str__(self):
        return f"{self.user.username}'s preference"  # 출력 시 사용자 이름과 조건 표시

class AdoptionMatch(models.Model):  # 추천 매칭 결과를 저장하는 모델
    user = models.ForeignKey(  # 입양을 원하는 사용자
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    cat = models.ForeignKey(  # 매칭된 고양이
        Cat,
        on_delete=models.CASCADE
    )
    matched_at = models.DateTimeField(auto_now_add=True)  # 매칭된 시점 기록

    def __str__(self):
        return f"{self.user.username} ↔ {self.cat.name}"  # 예: 'kim ↔ 나비'