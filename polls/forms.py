from django import forms


class TextForm(forms.Form):
    text = forms.CharField(label='Inserisci la porzione di testo da cercare...', max_length=100)
