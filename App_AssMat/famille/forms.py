from pyexpat import model
from django import forms

from famille.models import Employeur, ContactUrgence

class NewEmployeurForm(forms.ModelForm):
    """"""
    class Meta:
        model = Employeur
        fields = ['nom', 
                  'prenom',
                  'email',
                  'photo',
                  'adresse_postale'
                  ,'code_postal',
                  'ville', 
                  'tel_fix', 
                  'tel_mob', 
                  'tel_doc', 
                  'date_anniv', 
                  'num_urssaf'
                  ]

        
class NewContactUrgenceForm(forms.ModelForm):
    """"""
    class Meta:
        model = ContactUrgence
        fields = ['nom', 
                  'prenom', 
                  'filiation', 
                  'tel_fix', 
                  'tel_mob', 
                  'employeur'
                  ]
        