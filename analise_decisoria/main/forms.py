from django import forms

class captura_entrada_form(forms.Form):
    qtdeCriterio    = forms.IntegerField()
    qtdeAlternativa = forms.IntegerField()
<<<<<<< HEAD

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
=======
class FocoPrincipal_Form(forms.Form):
    focoPrincipal = forms.CharField(label='Foco Principal', max_length=100)
>>>>>>> e1de9d24a032e4cb08b1439df9710aadd1fe730e
