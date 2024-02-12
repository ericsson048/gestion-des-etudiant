from django import forms
from .models import Etudiant


class EtudiantForm(forms.Form):
    etudiant = forms.ModelChoiceField(queryset=Etudiant.objects.all())
