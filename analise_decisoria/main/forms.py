from django import forms
from django.db import models

class captura_entrada_form(forms.Form):
    qtdeCriterio    = forms.IntegerField(min_value=2, max_value=99)
    qtdeAlternativa = forms.IntegerField(min_value=2, max_value=99)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class FocoPrincipal_Form(forms.Form):
    focoPrincipal = forms.CharField(label='Foco Principal', max_length=100)

class Criterio_AHP_Form(forms.Form):
    criterio = forms.CharField(label='Criterio', max_length=100)

class Alternativa_AHP_Form(forms.Form):
    alternativa = forms.CharField(label='Alternativa', max_length=100)

class captura_entrada_AHP_Form(forms.Form):
    qtdeCriterio    = forms.IntegerField(min_value=2, max_value=10)
    qtdeAlternativa = forms.IntegerField(min_value=2, max_value=10)
    focoPrincipal = forms.CharField(max_length=100)
