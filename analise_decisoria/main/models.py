from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class captura_entrada(models.Model):
    qtdeCriterio    =  models.CharField(max_length=3)
    qtdeAlternativa =  models.CharField(max_length=3)

    def __str__(self):
        return self.qtdeCriterio
