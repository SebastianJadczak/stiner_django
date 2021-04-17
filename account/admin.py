from django.contrib import admin
from .models import Profile, Preference


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.get_fields()]


@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Preference._meta.get_fields()]
