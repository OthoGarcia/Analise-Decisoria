from django import forms

class captura_entrada_form(forms.Form):
    qtdeCriterio    = forms.IntegerField()
    qtdeAlternativa = forms.IntegerField()
