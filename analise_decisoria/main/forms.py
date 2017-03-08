from django import forms
from django.forms import formsets
class captura_entrada_form(forms.Form):
    qtdeCriterio    = forms.IntegerField(required=True, min_value=2, max_value=99)
    qtdeAlternativa = forms.IntegerField(required=True, min_value=2, max_value=99)

class montaVetorCriterio(forms.Form):
    criterio    = forms.CharField(required=True, max_length=100)

class montaVetorAlternativa(forms.Form):
    alternativa = forms.CharField(required=True, max_length=100)

class montaVetorPeso(forms.Form):
    pesos = forms.FloatField(required=True, min_value=0.1, max_value=1)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class Criterio_AHP_Form(forms.Form):
    criterio = forms.CharField(label='Criterio', max_length=100)

CriterioFormSet = formsets.formset_factory(Criterio_AHP_Form, min_num=1, max_num=10)

class Alternativa_AHP_Form(forms.Form):
    alternativa = forms.CharField(label='Alternativa', max_length=100)

class captura_entrada_AHP_Form(forms.Form):
    qtdeCriterio    = forms.IntegerField(min_value=2, max_value=10)
    qtdeAlternativa = forms.IntegerField(min_value=2, max_value=10)
    focoPrincipal = forms.CharField(max_length=100)
