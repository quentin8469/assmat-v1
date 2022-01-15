from django.db import models
from django.urls import reverse
from account.models import CustomUser

# Create your models here.
class Employeur(models.Model):
    email = models.EmailField(max_length=40, blank=True, null=True)
    photo = models.ImageField(upload_to="photo_profil/", blank=True, null=True)
    nom = models.CharField(max_length=40, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    adresse_postale = models.CharField(max_length=40, blank=True, null=True)
    code_postal =models.CharField(max_length=5, blank=True, null=True)
    ville = models.CharField(max_length=40, blank=True, null=True)
    tel_fix = models.CharField(max_length=10, blank=True, null=True)
    tel_mob = models.CharField(max_length=10, blank=True, null=True)
    tel_doc = models.CharField(max_length=10, blank=True, null=True)
    date_anniv = models.DateTimeField(blank=True, null=True)
    num_urssaf = models.CharField(max_length=13, blank=True, null=True)
    ass_mat = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Employeur"
        verbose_name_plural = "Employeurs"

    def __str__(self):
        return f"{self.nom} - {self.prenom}"
    
    


class Famille(models.Model):
    pass

class ContactUrgence(models.Model):
    nom = models.CharField(max_length=40, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    filiation = models.CharField(max_length=20, blank=True, null=True)
    tel_fix = models.CharField(max_length=10, blank=True, null=True)
    tel_mob = models.CharField(max_length=10, blank=True, null=True)
    employeur = models.ForeignKey(to=Employeur, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Contact Urgence"
        verbose_name_plural = "Contacts Urgences"

    def __str__(self):
        return f"{self.nom} - {self.prenom}"