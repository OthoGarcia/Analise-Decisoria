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
            return render(request, 'ahp/ahp_informaCriterioAlternativa.html', {'focoPrincipal': focoPrincipal, 'qtdeCriterio': qtdeCriterio, 'qtdeAlternativa' : qtdeAlternativa } )
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
    alternativa = []
    criterios = []
    pesos = []
    sinal = []
    tabela= []
    for i in range(len(data)-2):
        if i != 0 :
            alternativa.append(data[i][0])
    for i in range(1,len(data[0])):
        pesos.append(data[len(data)-2][i])
        criterios.append(data[0][i])
        sinal.append(data[len(data)-1][i])
    for i in range(1,len(data)-2):
        linha=[]
        if i != 0 :
            for j in range(1,len(data[0])):
                linha.append(data[i][j])
            tabela.append(linha)
    teste = len(tabela[0])
    mCon = matrizConcordanciaI(alternativa, tabela, len(tabela), len(tabela[0]), pesos)
    mDes = matrizDiscordanciaI(alternativa,tabela, len(tabela),  len(tabela[0]))
    return render(request,'main/dados.html', {'dados': alternativa, 'nLinhas': len(tabela[0])-1})


def matrizConcordanciaI(cidades, tabela, nLinhas, nColunas, vetorPesos):

	somaPesos = 0
	mConcordancia = []

	for x in range(len(vetorPesos)):
		somaPesos += float(vetorPesos[x].replace(',','.'))


	for i in range(nLinhas):
		linha = []
		for j in range(len(tabela[i])):

			somatorioW = 0
			for y in range(nColunas):
				if tabela[i][y] >= tabela[j][y]:
					somatorioW += float(vetorPesos[y].replace(',','.'))
			result = 1.0/somaPesos * somatorioW
			linha.append(round(result, 2))

		mConcordancia.append(linha)
	return mConcordancia

def matrizDiscordanciaI(cidades, tabela, nLinhas, nColunas):
	vetorDiferencas = []

	for i in range(nLinhas):
		valoresCriterio = []
		for j in range(len(tabela[i])):
			valoresCriterio.append(int(tabela[j][i]))
		valorMin = min(valoresCriterio)
		valorMax = max(valoresCriterio)
		result = valorMax - valorMin
		vetorDiferencas.append(result)


	mDiscordancia = []

	for i in range(nLinhas):
		linha = []
		for j in range(len(tabela[i])):
			vetorIndices = []
			for y in range(nColunas):
				vResultante = (float(tabela[j][y]) - float(tabela[i][y]))/vetorDiferencas[y]
				vetorIndices.append(round(vResultante, 2))
			linha.append(max(vetorIndices))
		mDiscordancia.append(linha)
		print mDiscordancia[i], cidades[i]
	return mDiscordancia
