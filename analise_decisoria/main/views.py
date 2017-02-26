from django.shortcuts import render, redirect
from .forms import captura_entrada_form, FocoPrincipal_Form

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
    return render(request, 'ahp/ahp_insert_valores.html', {})

def ahp_resultado(request):
    resultado=request.POST['focoPrincipal']
    return render(request, 'ahp/ahp_resultado.html', {'resultado': resultado})

def ahp_foco_principal(request):
    return render(request, 'ahp/ahp_foco_principal.html', {'form': FocoPrincipal_Form()})

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
