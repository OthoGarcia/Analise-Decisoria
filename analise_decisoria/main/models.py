from django.db import models


class captura_entrada(model.models):
    qtdeCriterio    =  models.CharField(max_length=3, validators=[numeric])
    qtdeAlternativa =  models.CharField(max_length=3, validators=[numeric])
