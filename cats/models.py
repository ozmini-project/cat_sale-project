from django.db import models
from users.models import CustomUser

class Cat(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)  # ✅ ERD에 있음
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cats')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.breed})"
