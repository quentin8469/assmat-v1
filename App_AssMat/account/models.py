from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
from account.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=40)
    photo = models.ImageField(upload_to="photo_profil/", blank=True, null=True)
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=20)
    adresse_postale = models.CharField(max_length=40)
    code_postal =models.CharField(max_length=5)
    ville = models.CharField(max_length=40)
    tel_fix = models.CharField(max_length=10)
    tel_mob = models.CharField(max_length=10)
    date_anniv = models.DateField()
    num_secu = models.CharField(max_length=13)
    max_enfants = models.IntegerField()
    num_agrement = models.CharField(max_length=6)
    date_agrement = models.DateField()
    ass_civil = models.CharField(max_length=20)
    ass_auto = models.CharField(max_length=20)
    
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