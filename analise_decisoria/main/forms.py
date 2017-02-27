from django import forms

class captura_entrada_form(forms.Form):
    qtdeCriterio    = forms.IntegerField()
    qtdeAlternativa = forms.IntegerField()

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class FocoPrincipal_Form(forms.Form):
    focoPrincipal = forms.CharField(label='Foco Principal', max_length=100)
