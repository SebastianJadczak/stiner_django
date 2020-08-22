
from django import forms
from django.contrib.auth.models import User

class FormularzRejestracji(forms.ModelForm):
    username = forms.CharField(label="Login:", max_length=30, widget=forms.TextInput(attrs={'class': 'username_register first', }))
    email = forms.EmailField(label="Email:",widget=forms.TextInput(attrs={'class': 'username_register'}))
    password = forms.CharField(label='Hasło:', widget=forms.PasswordInput(attrs={'class': 'username_register'}))

    #Klasa dzięki czemu użytkownikom nie są dodawane 's' na końcu
    class Meta:
        model = User
        fields = ['username', 'email', 'password']