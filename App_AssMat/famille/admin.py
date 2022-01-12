from django.contrib import admin

# Register your models here.
from famille.models import Employeur, Famille, ContactUrgence

@admin.register(Employeur)
class EmployeurAdmin(admin.ModelAdmin):
    list_display = ('nom', "prenom", "ass_mat")
    
@admin.register(Famille)
class FamilleAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactUrgence)
class ContactUrgenceAdmin(admin.ModelAdmin):
    list_display = ('nom', "prenom", "filiation", "employeur")
