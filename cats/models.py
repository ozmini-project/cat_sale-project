from django.db import models  # Django 모델 관련 모듈
from django.conf import settings  # settings.AUTH_USER_MODEL을 사용하기 위해

class Cat(models.Model):  # 고양이 정보를 저장하는 모델
    GENDER_CHOICES = [  # 성별을 선택지로 제공 (M: 수컷, F: 암컷)
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)  # 고양이 이름 (최대 100자)
    breed = models.CharField(max_length=50)  # 품종 (예: 코숏, 러시안블루 등)
    age = models.PositiveIntegerField()  # 나이 (0 이상 양수만 가능)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)  # M 또는 F 중 선택
    description = models.TextField(blank=True)  # 고양이 설명 (비워도 됨)
    owner = models.ForeignKey(  # 고양이 등록자 (사용자와 연결됨)
        settings.AUTH_USER_MODEL,  # 커스텀 사용자 모델과 연결
        on_delete=models.CASCADE,  # 사용자 삭제 시 고양이도 삭제
        related_name='cats'  # user.cats로 이 유저의 고양이 리스트에 접근 가능
    )
    created_at = models.DateTimeField(auto_now_add=True)  # 등록일시 자동 저장

    def __str__(self):
        return self.name  # 고양이 이름을 출력용 문자열로 사용