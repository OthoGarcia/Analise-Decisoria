from django.shortcuts import render, redirect, render_to_response
from django import forms
from .forms import captura_entrada_form, UploadFileForm, captura_entrada_AHP_Form, Criterio_AHP_Form, Alternativa_AHP_Form, montaVetorCriterio, montaVetorAlternativa, montaVetorPeso
import csv
from django.template.context_processors import csrf
from django.forms import formset_factory
import itertools

# Create your views here.
def menu_principal(request):
    return render(request, 'main/menu_principal.html', {})

def insert_valores(request):
    return render(request, 'main/insert_valores.html', {})

def resultado_matriz(request):
    return render(request, 'main/resultado_matriz.html', {})

def sobre(request):
    return render(request, 'main/sobre.html', {})

def ahp_informaCriterioAlternativa(request):
    CriterioFormSet    = formset_factory(Criterio_AHP_Form)
    AlternativaFormSet = formset_factory(Alternativa_AHP_Form)
    if request.method == 'POST':
        criterioFormSet    = CriterioFormSet(request.POST, prefix='Criterio')
        alternativaFormSet = AlternativaFormSet(request.POST, prefix='Alternativa')
        if criterioFormSet.is_valid() and alternativaFormSet.is_valid():
            resultado='Funcionou!'
            return render(request, 'ahp/ahp_resultado.html', {'resultado': resultado} )
        else:
            criterioFormSet    = CriterioFormSet(prefix='Criterio')
            alternativaFormSet = AlternativaFormSet(prefix='Alternativa')
            return render(request, 'ahp/ahp_informaCriterioAlternativa.html', {'criterioFormSet': criterioFormSet, 'alternativaFormSet' : alternativaFormSet } )


def informaCriterioAlternativa(request):
    CriterioFormSet    = formset_factory(montaVetorCriterio)
    AlternativaFormSet = formset_factory(montaVetorAlternativa)
    if request.method == 'POST':
        criterioFormSet    = CriterioFormSet(request.POST, prefix='Criterio')
        alternativaFormSet = AlternativaFormSet(request.POST, prefix='Alternativa')
        if criterioFormSet.is_valid() and alternativaFormSet.is_valid():
            resultado='Funcionou!'
            return render(request, 'main/resultado_matriz.html', {'resultado': resultado} )
        else:
            criterioFormSet    = CriterioFormSet(prefix='Criterio')
            alternativaFormSet = AlternativaFormSet(prefix='Alternativa')
            return render(request, 'main/informaCriterioAlternativa.html', {'criterioFormSet': criterioFormSet, 'alternativaFormSet' : alternativaFormSet } )

def ahp_insert_valores(request):
    if request.method == 'POST':
        formCapEntra     = captura_entrada_AHP_Form(request.POST)
        focoPrincipal    = request.POST['focoPrincipal']
        qtdeAlternativa  = request.POST['qtdeAlternativa']
        qtdeCriterio     = request.POST['qtdeCriterio']

        if formCapEntra.is_valid():
            criterioFormSet    = formset_factory(Criterio_AHP_Form, extra=int(qtdeCriterio))
            alternativaFormSet = formset_factory(Alternativa_AHP_Form, extra=int(qtdeAlternativa))
            return render(request, 'ahp/ahp_informaCriterioAlternativa.html', {'criterioFormSet': criterioFormSet, 'alternativaFormSet' : alternativaFormSet } )
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
            criterioFormSet    = formset_factory(montaVetorCriterio, extra=int(qtdeCriterio))
            alternativaFormSet = formset_factory(montaVetorAlternativa, extra=int(qtdeAlternativa))
            pesoFormSet        = formset_factory(montaVetorPeso, extra=int(qtdeCriterio))
            return render(request, 'main/informaCriterioAlternativa.html', {'criterioFormSet': criterioFormSet, 'alternativaFormSet' : alternativaFormSet, 'pesoFormSet' : pesoFormSet } )
        else:
			return render(request, 'main/qtdeCriterioAlternativa.html',{'form': form})
    else:
		return render(request, 'main/qtdeCriterioAlternativa.html',{'form': captura_entrada_form()})

def getAlternativas (request):
    alternativas= []
    for i in range(0,4):
        alternativas.append(request.POST['form-'+str(i)+'-alternativa'])
    print alternativas
    return render(request, 'main/teste.html')

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
    iterator=itertools.count()
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
    c = float(data[len(data)-1][1].replace(',','.'))
    d = float(data[len(data)-1][2].replace(',','.'))

    teste = len(tabela[0])
    mCon = matrizConcordanciaI(alternativa, tabela, len(tabela), len(tabela[0]), pesos)
    mDes = matrizDiscordanciaI(alternativa,tabela, len(tabela),  len(tabela[0]))
    mVeto = calculaMveto(mCon, mDes, c, d, len(tabela))
    kernel = calculaKernel(mVeto, len(tabela), alternativa )
    result = []
    for i in range(len(tabela)):
        for j in range(len(tabela[i])+1):
            if j==0:
                result.append(alternativa[i])
            else:
                result.append(tabela[i][j-1])
    print result
    return render(request,'main/dados.html', {'alternativas': alternativa, 'criterios': criterios, 'tabela': tabela, 'mCon': mCon, 'i': len(tabela[i])+1 , 'result': result })


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

def calculaMveto(mConcordanciaI, mDiscordanciaI, c, d, nLinhas):
    matrizVeto = []
    for i in range(nLinhas):
        linha = []
        for j in range(len(mConcordanciaI[i])):
            if (mConcordanciaI[i][j] >= c) and (mDiscordanciaI[i][j] <= d):
                linha.append(1)
            else:
                linha.append(0)
        matrizVeto.append(linha)
    return matrizVeto


def calculaKernel(matrizVeto,nLinhas, cidades):
    matrizSobreclassifica = []
    for i in range(nLinhas):
        linha = []
        for j in range(len(matrizVeto[i])):
            if matrizVeto[i][j] == 1 and i!=j:
                linha.append(j)
        matrizSobreclassifica.append(linha)
    kernel = []
    print "\nKernel\n"

    for k in range(nLinhas):
        achou = False
        vazio = False
        for i in range(nLinhas):
            for j in range(len(matrizSobreclassifica[i])):
                if matrizSobreclassifica[i][j] == k:
                    achou = True
                if not matrizSobreclassifica[i]:
                    vazio = True
                if (achou == False) and (vazio == False):
                    if cidades[k] not in kernel:
                        kernel.append(cidades[k])
    return kernel
