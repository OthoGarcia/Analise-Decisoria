from django import forms

class captura_entrada_form(forms.Form):
    qtdeCriterio    = forms.IntegerField()
    qtdeAlternativa = forms.IntegerField()
class FocoPrincipal_Form(forms.Form):
    focoPrincipal = forms.CharField(label='Foco Principal', max_length=100)
