from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
from account.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=40)
    photo = models.ImageField(upload_to="photo_profil/", blank=True, null=True)
    nom = models.CharField(max_length=40, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    adresse_postale = models.CharField(max_length=40, blank=True, null=True)
    code_postal =models.CharField(max_length=5, blank=True, null=True)
    ville = models.CharField(max_length=40, blank=True, null=True)
    tel_fix = models.CharField(max_length=10, blank=True, null=True)
    tel_mob = models.CharField(max_length=10, blank=True, null=True)
    date_anniv = models.CharField(max_length=10, blank=True, null=True)
    num_secu = models.CharField(max_length=13, blank=True, null=True)
    max_enfants = models.IntegerField(blank=True, null=True)
    num_agrement = models.CharField(max_length=6, blank=True, null=True)
    date_agrement = models.CharField(max_length=10, blank=True, null=True)
    ass_civil = models.CharField(max_length=20, blank=True, null=True)
    ass_auto = models.CharField(max_length=20, blank=True, null=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    object = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username