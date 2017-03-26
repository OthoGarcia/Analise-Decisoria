from django.shortcuts import render, redirect, render_to_response
from django import forms
from .forms import captura_entrada_form, UploadFileForm, captura_entrada_AHP_Form, Criterio_AHP_Form, Alternativa_AHP_Form, montaVetorCriterio, montaVetorAlternativa, montaVetorPeso, CriterioFormSet
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
    qtdeAlternativa  = request.POST['qtdeAlternativa']
    qtdeCriterio     = request.POST['qtdeCriterio']
    CriterioFormSet    = formset_factory(Criterio_AHP_Form, extra=int(qtdeCriterio))
    AlternativaFormSet = formset_factory(Alternativa_AHP_Form, extra=int(qtdeAlternativa))
    criterioFormSet    = CriterioFormSet(prefix='Criterio')
    alternativaFormSet = AlternativaFormSet(prefix='Alternativa')
    return render(request, 'ahp/ahp_informaCriterioAlternativa.html', {'criterioFormSet': criterioFormSet, 'alternativaFormSet' : alternativaFormSet } )

def ahp_insert_valores(request):
    if request.method == 'POST':
        formCapEntra     = captura_entrada_AHP_Form(request.POST)
        qtdeAlternativa  = request.POST['qtdeAlternativa']
        qtdeCriterio     = request.POST['qtdeCriterio']

        if formCapEntra.is_valid():
            return render(request, 'ahp/ahp_informaCriterioAlternativa.html', {} )
        else:
            return render(request, 'ahp/ahp_insert_valores.html',{'form': formCapEntra})
    else:
        return render(request, 'ahp/ahp_insert_valores.html',{'form': captura_entrada_AHP_Form()})

def ahp_resultado(request):
    if request.method == 'POST':
        criterio_formset = CriterioFormSet(request.POST, prefix='criterio_form')
        if criterio_formset.is_valid():
            resultado={}
            x=1
            for criin in criterio_formset:
                resultado[str(x)]=criin['criterio']
                x+=1
            return render(request, 'ahp/ahp_resultado.html', {'resultado': resultado})
        else:
            return render(request, 'ahp/ahp_teste.html', {'criterio_formset': criterio_formset})
    return render(request, 'ahp/ahp_resultado.html', {'resultado': request.POST.keys()})

def teste(request):
    if request.method == 'POST':
        criterio_formset = CriterioFormSet(request.POST, prefix='criterio_form')
        if criterio_formset.is_valid():
            return render(request, 'ahp/ahp_resultado.html', {'resultado': criterio_formset.keys()})
        else:
            return render(request, 'ahp/ahp_teste.html', {'criterio_formset': criterio_formset})
    return render(request, 'ahp/ahp_teste.html', {'criterio_formset': CriterioFormSet(prefix='criterio_form')})

def qtdeCriterioAlternativa (request):
    if request.method   == 'POST':
        formCapEntra     = captura_entrada_form(request.POST)

        request.session['qtdeAlternativa']  = request.POST['qtdeAlternativa']
        request.session['qtdeCriterio']     = request.POST['qtdeCriterio']

        qtdeAlternativa  = request.POST['qtdeAlternativa']
        qtdeCriterio     = request.POST['qtdeCriterio']

        if formCapEntra.is_valid():
            criterioFormSet    = formset_factory(montaVetorCriterio, extra=int(qtdeCriterio))
            alternativaFormSet = formset_factory(montaVetorAlternativa, extra=int(qtdeAlternativa))
            pesoFormSet        = formset_factory(montaVetorPeso, extra=int(qtdeCriterio))
            return render(request, 'main/informaCriterioAlternativa.html', {'criterioFormSet': criterioFormSet, 'alternativaFormSet' : alternativaFormSet, 'pesoFormSet' : pesoFormSet, 'alternativa' : qtdeAlternativa, 'criterio' : qtdeCriterio } )
        else:
			return render(request, 'main/qtdeCriterioAlternativa.html',{'form': form})
    else:
		return render(request, 'main/qtdeCriterioAlternativa.html',{'form': captura_entrada_form()})

def getAlternativas (request):
    if request.method   == 'POST':
        alternativas    = []
        criterios       = []
        request.session['pesos']       = []
        request.session['alternativa'] = []
        request.session['criterio']    = []
        qtdeAlternativa = request.POST['alternativa']
        qtdeCriterio    = request.POST['criterio']

        for i in range(0,int(request.session['qtdeAlternativa'])):
            alternativas.append(request.POST['form-'+str(i)+'-alternativa'])
            request.session['alternativa'].append(request.POST['form-'+str(i)+'-alternativa'])

        for i in range(0,int(request.session['qtdeCriterio'])):
            criterios.append(request.POST['form-'+str(i)+'-criterio'])
            request.session['criterio'].append(request.POST['form-'+str(i)+'-criterio'])

        for i in range(0,int(request.session['qtdeCriterio'])):
            request.session['pesos'].append(request.POST['form-'+str(i)+'-pesos'])

        return render(request, 'main/preencheMatriz.html', {'alternativas' : alternativas, 'criterios' : criterios})

    else:
		return render(request, 'main/informaCriterioAlternativa.html')

def preencheMatriz (request):

    tabela = []
    mCon   = []
    mDes   = []

    for i in range(int(request.session['qtdeCriterio'])):
        linha=[]
        for j in range(int(request.session['qtdeAlternativa'])):
            linha.append(request.POST['Criterio'+str(i)+'-Alternativa'+str(j)])
        tabela.append(linha)

    mCon = matrizConcordanciaI(request.session['alternativa'], tabela, len(tabela), len(tabela[0]), request.session['pesos'])
    mDes = matrizDiscordanciaI(request.session['alternativa'], tabela, len(tabela), len(tabela[0]))
    '''mVeto = calculaMveto(mCon, mDes, c, d, len(tabela))
    kernel = calculaKernel(mVeto, len(tabela), alternativa )
    '''
    result    = []
    resultCon = []
    resultDes = []
    for i in range(len(tabela)):
        for j in range(len(tabela[i])+1):
            if j==0:
                result.append(request.session['alternativa'][i])
                resultCon.append(request.session['alternativa'][i])
                resultDes.append(request.session['alternativa'][i])
            else:
                result.append(tabela[i][j-1])
                if (i != j-1):
                    resultCon.append(mCon[i][j-1])
                    resultDes.append(mDes[i][j-1])
                else:
                    resultCon.append('-')
                    resultDes.append('-')
    return render(request,'main/dados.html', {'alternativas': request.session['alternativa'],'tabela': tabela, 'criterios': request.session['criterio'], 'mDes': resultDes, 'mCon': resultCon, 'i': len(tabela[i])+1 , 'result': result })

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
    resultCon = []
    resultDes = []
    resultMveto = []
    for i in range(len(tabela)):
        for j in range(len(tabela[i])+1):
            if j==0:
                result.append(alternativa[i])
            else:
                result.append(tabela[i][j-1])
    for i in range(len(tabela)):
        for j in range(len(tabela)+1):
            if j==0:
                resultCon.append(alternativa[i])
                resultDes.append(alternativa[i])
                resultMveto.append(alternativa[i])
            else:
                if (i != j-1):
                    resultCon.append(mCon[i][j-1])
                    resultDes.append(mDes[i][j-1])
                    resultMveto.append(mDes[i][j-1])
                else:
                    resultCon.append('-')
                    resultMveto.append('-')
                    resultDes.append('-')

    return render(request,'main/dados.html', {'kernel': kernel,'mVeto': resultMveto,'alternativas': alternativa,'tabela': tabela, 'criterios': criterios, 'mDes': resultDes, 'mCon': resultCon, 'i': len(tabela)+1 ,'iT': len(tabela[i])+1,  'result': result })


def matrizConcordanciaI(cidades, tabela, nLinhas, nColunas, vetorPesos):
    somaPesos = 0
    mConcordancia = []
    for x in range(len(vetorPesos)):
        somaPesos += float(vetorPesos[x].replace(',','.'))
    for i in range(0,nLinhas):
        linha = []
        for j in range(0,nLinhas):
            if i == j :
                linha.append(1)
            else :
                somatorioW = 0
                for y in range(nColunas):
                    if int(tabela[i][y]) >= int(tabela[j][y]):
                        somatorioW += float(vetorPesos[y].replace(',','.'))/somaPesos
                    '''print('i='+str(i)+'j='+str(j)+'y='+str(y)+str(tabela[i][y])+'>'+str(tabela[j][y]))
                    print(str(somatorioW))
                    print(float(vetorPesos[y].replace(',','.'))/somaPesos)'''
                print('_____________')
                linha.append(round(somatorioW, 2))
        mConcordancia.append(linha)
    return mConcordancia

def matrizDiscordanciaI(cidades, tabela, nLinhas, nColunas):
    vetorDiferencas = []
    mDiscordancia = []
    for i in range(0,nColunas):
        valoresCriterio = []
        for j in range(0,nLinhas):
            valoresCriterio.append(int(tabela[j][i]))
        valorMin = min(valoresCriterio)
        valorMax = max(valoresCriterio)
        result = valorMax - valorMin
        vetorDiferencas.append(result)

    for i in range(0,nLinhas):
        linha = []
        for j in range(0,nLinhas):
            vetorIndices = []
            for y in range(nColunas):
                vResultante = (float(tabela[i][y]) - float(tabela[j][y]))/vetorDiferencas[y]
                vetorIndices.append(round(vResultante, 2))
                print('i='+str(i)+'j='+str(j)+'y='+str(y))
            linha.append(max(vetorIndices))
        mDiscordancia.append(linha)
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
