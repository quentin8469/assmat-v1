from django.db import models

from famille.models import Employeur

# Create your models here.
class TypeContrat(models.Model):
    
    choix_titre = [('cdi', 'Cdi'),
                     ('cdd', 'Cdd'),
                     ('occasionnel', 'Occasionnel')]
    
    titre = models.CharField(max_length=50, choices=choix_titre)
    
    class Meta:
        verbose_name = "Titre"
        verbose_name_plural = "Titres"
    
    def __str__(self):
        return f"{self.titre}"


class Contrat(models.Model):
    nom = models.CharField(max_length=40, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_debut = models.DateTimeField(blank=True, null=True)
    date_fin = models.DateTimeField(blank=True, null=True)
    heure_hebdo = models.IntegerField(blank=True, null=True)
    jour_hebdo = models.IntegerField(blank=True, null=True)
    nb_semaine = models.IntegerField(blank=True, null=True)
    date_paiement = models.DateTimeField(blank=True, null=True)
    type_contrat = models.ForeignKey(to=TypeContrat, on_delete=models.CASCADE)
    employeur = models.ForeignKey(to=Employeur, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Contrat"
        verbose_name_plural = "Contrats"

    def __str__(self):
        return f"{self.nom} - {self.employeur}"


class Enfant(models.Model):
    photo = models.ImageField(upload_to="photo_profil/", blank=True, null=True)
    nom = models.CharField(max_length=40, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    date_anniv = models.DateTimeField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    commentaire = models.TextField(blank=True, null=True)
    contrat = models.ForeignKey(to=Contrat, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Enfant"
        verbose_name_plural = "Enfants"

    def __str__(self):
        return f"{self.nom} - {self.prenom}"
    
        
class Remuneration(models.Model):
    base_mensuel = models.FloatField(blank=True, null=True)
    heure_mensuel = models.FloatField(blank=True, null=True)
    taux_h_brut = models.FloatField(blank=True, null=True)
    taux_h_net = models.FloatField(blank=True, null=True)
    jour_mensuel = models.FloatField(blank=True, null=True)
    contrat = models.ForeignKey(to=Contrat, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = "Remuneration"
        verbose_name_plural = "Remunerations"

    def __str__(self):
        return f"{self.contrat}"
    

class CongePaye(models.Model):
    maintient_salaire = models.FloatField(blank=True, null=True)
    dix_pourcent = models.FloatField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Congé Payé"
        verbose_name_plural = "Congés Payés"

    def __str__(self):
        return f"{self.maintient_salaire} - {self.dix_pourcent}"