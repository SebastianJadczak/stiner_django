from django import forms

class EmailForm(forms.Form):
    """ Formularz wysyłania wiadomości email """

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)