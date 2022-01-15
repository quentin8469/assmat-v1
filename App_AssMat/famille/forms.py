from django import forms

from famille.models import Employeur

class NewEmployeurForm(forms.ModelForm):
    """"""
    class Meta:
        model = Employeur
        fields = ['nom', 'prenom','email','photo','adresse_postale'
                  ,'code_postal','ville', 'tel_fix', 'tel_mob', 'tel_doc', 
                  'date_anniv', 'num_urssaf']