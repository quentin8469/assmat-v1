from django.contrib import admin

# Register your models here.
from contrat.models import TypeContrat, Contrat, Remuneration, CongePaye, Enfant

@admin.register(TypeContrat)
class TypeContratAdmin(admin.ModelAdmin):
    list_display = ('titre',)
    

@admin.register(Contrat)
class ContratAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_contrat', 'employeur')
    

@admin.register(Remuneration)
class RemunerationAdmin(admin.ModelAdmin):
    list_display = ('base_mensuel', 'contrat')

@admin.register(CongePaye)
class CongePayeAdmin(admin.ModelAdmin):
    list_display = ('maintient_salaire', 'dix_pourcent')
    

@admin.register(Enfant)
class EnfantAdmin(admin.ModelAdmin):
    list_display = ('nom', "prenom", "age")