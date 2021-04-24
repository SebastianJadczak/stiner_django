from django import forms

from .models import Profile, Preference

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = "__all__"

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"

