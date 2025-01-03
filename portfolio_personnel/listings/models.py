from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Groupe(models.Model):
    
    class Genre(models.TextChoices):
        HIP_HOP= "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"
        
    nom = models.fields.CharField(max_length=100)
    
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    
    biographie = models.fields.CharField(max_length=1000)
    annee_formation = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    actif = models.fields.BooleanField(default=True)
    page_officielle = models.fields.URLField(null=True, blank=True)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    annee = models.fields.IntegerField(null=True)
    def __str__(self):
        return f'{self.nom}'


class Article(models.Model):
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    annee = models.fields.IntegerField()
    groupe = models.ForeignKey(Groupe, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.title}"