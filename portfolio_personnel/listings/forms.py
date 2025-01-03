from django import forms
from listings.models import Groupe

class GroupeForm(forms.ModelForm):
    class Meta:
        model= Groupe
        exclude = ('actif', 'page_officielle')

class ContactUsForm(forms.Form):
    nom = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)