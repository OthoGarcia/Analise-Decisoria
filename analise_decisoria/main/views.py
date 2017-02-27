from django.shortcuts import render, redirect, render_to_response
from .forms import captura_entrada_form, FocoPrincipal_Form, UploadFileForm, captura_entrada_AHP_Form
import csv
from django.template.context_processors import csrf

# Create your views here.
def menu_principal(request):
    return render(request, 'main/menu_principal.html', {})

def insert_valores(request):
    return render(request, 'main/insert_valores.html', {})

def resultado_matriz(request):
    return render(request, 'main/resultado_matriz.html', {})

def sobre(request):
    return render(request, 'main/sobre.html', {})

def ahp_insert_valores(request):
    if request.method == 'POST':
        formCapEntra     = captura_entrada_AHP_Form(request.POST)
        focoPrincipal    = request.POST['focoPrincipal']
        qtdeAlternativa  = request.POST['qtdeAlternativa']
        qtdeCriterio     = request.POST['qtdeCriterio']

        if formCapEntra.is_valid():
            return render(request, 'main/informaCriterioAlternativa.html', {'qtdeCriterio': qtdeCriterio, 'qtdeAlternativa' : qtdeAlternativa } )
        else:
            return render(request, 'ahp/ahp_insert_valores.html',{'form': formCapEntra})
    else:
        return render(request, 'ahp/ahp_insert_valores.html',{'form': captura_entrada_AHP_Form()})

def ahp_resultado(request):
    resultado=request.POST['focoPrincipal']
    return render(request, 'ahp/ahp_resultado.html', {'resultado': resultado})

def qtdeCriterioAlternativa (request):
    if request.method   == 'POST':
        formCapEntra     = captura_entrada_form(request.POST)
        qtdeAlternativa  = request.POST['qtdeAlternativa']
        qtdeCriterio     = request.POST['qtdeCriterio']

        if formCapEntra.is_valid():
            return render(request, 'main/informaCriterioAlternativa.html', {'qtdeCriterio': qtdeCriterio, 'qtdeAlternativa' : qtdeAlternativa } )
        else:
			return render(request, 'main/qtdeCriterioAlternativa.html',{'form': form})
    else:
		return render(request, 'main/qtdeCriterioAlternativa.html',{'form': captura_entrada_form()})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_reader(request)
    else:
        form = UploadFileForm()
    return render(request, 'main/insert_tema_tamanho.html', {'arquivo': form})

def csv_reader(request):
    """
    Read a csv file
    """
    file = request.FILES['file']
    data = [row for row in csv.reader(file.read().splitlines())]
    return render(request,'main/dados.html', {'dados': data})
