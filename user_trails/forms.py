from django import forms
from .models import UserTrail


class UserTrailCreateForm(forms.ModelForm):
    """Klasa odpowiedzialna za tworzenie trasy użytkownika na podstawie modelu trasy użytkownika."""

    class Meta:
        model = UserTrail
        fields = ['user', 'name', 'descriptions']
        exclude = ["user"]
