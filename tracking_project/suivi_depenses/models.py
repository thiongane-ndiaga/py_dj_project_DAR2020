from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Suivi(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='suivis',null=True)
    slug = models.SlugField(max_length=100,unique=True,blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10,decimal_places=2)
    date_limite = models.DateField()
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.nom)
        super(Suivi, self).save(*args,**kwargs)

    def b_restant(self):
        return self.budget - self.d_totales()

    def d_totales(self):
        depenses = Depense.objects.filter(suivi=self)
        total = 0
        for d in depenses:
            total+=d.montant
        return total

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

class Depense(models.Model):
    suivi = models.ForeignKey(Suivi,on_delete=models.CASCADE, related_name='depenses')
    titre = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=8,decimal_places=2)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)

    class Meta:
        ordering = ("-montant",)
