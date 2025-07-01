from django.contrib import admin
from .models import Cat

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'breed', 'age', 'gender', 'owner']
    search_fields = ['name', 'breed']
    list_filter = ['breed', 'gender']
