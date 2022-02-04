from django import forms
from contrat.models import Contrat, Enfant

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


class NewEnfantForm(forms.ModelForm):
    """ from for the child creation """
    class Meta:
        model = Enfant
        fields = [
            'photo',
            'nom',
            'prenom',
            'date_anniv',
            'age',
            'commentaire',
            'contrat',
            
        ]