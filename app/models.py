import uuid
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
class UserProfilesManager(BaseUserManager):
    """ modele de management  de profile utilisateur"""

    def create_user(self, Email, Nom, Prenom, password=None):
        """ creation d'un profile utilisateur """
        if not Email:
            raise ValueError('un utilisateur doit avoir un mail')

        Email = self.normalize_email(Email)
        user = self.model(Email=Email, Nom=Nom, Prenom=Prenom)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, Email, Nom, Prenom, password):
        """creation d'un super utilisateur"""

        user = self.create_user(Email, Nom, Prenom, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    Email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_etudiant = models.BooleanField(default=False)
    is_professeur = models.BooleanField(default=False)

    objects = UserProfilesManager()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['Nom', 'Prenom']

    @property
    def nom(self):
        return str(self.Nom).upper()

    @property
    def prenom(self):
        return str(self.Prenom).capitalize()

    def __str__(self):
        return self.Nom + " /" + self.Prenom


class Etudiant(models.Model):
    CodeEtudiant = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    NomEtudiant = models.CharField(max_length=100)
    PrenomEtudiant = models.CharField(max_length=100)
    Matricule = models.CharField(max_length=255)
    DateNaissance = models.DateTimeField(blank=False)

    def __str__(self):
        return self.NomEtudiant

    @property
    def nom(self):
        return str(self.NomEtudiant).upper()

    @property
    def prenom(self):
        return str(self.PrenomEtudiant).capitalize()



class Cours(models.Model):
    CodeCours = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    NomCours = models.CharField(max_length=255)
    Volume = models.IntegerField(blank=False)

    def __str__(self):
        return self.NomCours


class Note(models.Model):
    CodeNote = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    createdOn=models.DateTimeField(auto_now=True)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['etudiant', 'cours'], name='unique_etudiant_cours')
        ]



    def __str__(self):
        return f"{self.etudiant.PrenomEtudiant} {self.etudiant.NomEtudiant} - {self.cours.NomCours}: {self.note}"
