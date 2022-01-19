from django import forms
from contrat.models import Contrat

class NewContratForm(forms.ModelForm):
    """"""
    class Meta:
        model = Contrat
        fields = [
            'nom',
            'date_debut',
            'date_fin',
            'heure_hebdo',
            'jour_hebdo',
            'nb_semaine',
            'date_paiement',
            'type_contrat',
            'employeur'
            
        ]