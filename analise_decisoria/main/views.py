from django.shortcuts import render, redirect

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

def qtdeCriterioAlternativa (request):
    if request.method == 'POST':
        formCapEntra  = captura_entrada_form(request.POST)
        if formCapEntra.is_valid():
            formCapEntra.save()
            return redirect('sobre')
        else:
			return render(request, 'main/qtdeCriterioAlternativa.html',{'form': form})
    else:
		return render(request, 'main/qtdeCriterioAlternativa.html',{'form': captura_entrada_form()})
