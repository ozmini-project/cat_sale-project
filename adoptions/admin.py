from django.contrib import admin
from .models import AdoptionMatch,AdoptionPreference

@admin.register(AdoptionMatch)
class AdoptionMatchAdmin(admin.ModelAdmin):
    pass

@admin.register(AdoptionPreference)
class AdoptionPreferenceAdmin(admin.ModelAdmin):
    pass


