from django import forms
from .models import casaModel

class CasaForm(forms.ModelForm):
    class Meta:
        model = casaModel.Casa
        fields = ['numero', 'foto']