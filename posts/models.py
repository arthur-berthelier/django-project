from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:20] #retourne les 20 premiers char du texte
