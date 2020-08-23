from django import forms

class EmailForm(forms.Form):
    """ Formularz wysyłania wiadomości email """

    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Podaj swoje imię', 'class' : 'name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Podaj swój adres email', 'class' : 'email'}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Tu wpisz wiadomość do Nas.', 'class' : 'text'}))