from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Reset, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import captura_entrada
from django.forms.models import inlineformset_factory

class captura_entrada_form(forms.ModelForm):
    class Meta:
        model  = captura_entrada
        fields = ['qtdeCriterio', 'qtdeAlternativa']
