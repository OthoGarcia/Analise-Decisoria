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

def electreIII (request):
    if request.method   == 'POST':
        formCapEntra     = captura_entrada_form(request.POST)
        qtdeAlternativa  = request.POST['qtdeAlternativa']
        qtdeCriterio     = request.POST['qtdeCriterio']

        if formCapEntra.is_valid():
            criterioFormSet    = formset_factory(montaVetorCriterio, extra=int(qtdeCriterio))
            alternativaFormSet = formset_factory(montaVetorAlternativa, extra=int(qtdeAlternativa))
            pesoFormSet        = formset_factory(montaVetorPeso, extra=int(qtdeCriterio))
            return render(request, 'main/electreIII_valores.html', {'criterioFormSet': criterioFormSet, 'alternativaFormSet' : alternativaFormSet, 'pesoFormSet' : pesoFormSet, 'alternativa' : qtdeAlternativa, 'criterio' : qtdeCriterio } )
        else:
            return render(request, 'main/electreIII.html',{'form': form})
    else:
        return render(request, 'main/electreIII.html',{'form': captura_entrada_form()})

def electreIII_valores (request):
    if request.method   == 'POST':
        riterioFormSet.montaVetorCriterio
        formCapEntra     = captura_entrada_form(request.POST)
        qtdeAlternativa  = request.POST['qtdeAlternativa']
        qtdeCriterio     = request.POST['qtdeCriterio']

        if formCapEntra.is_valid():
            indice_concordanciaFormSet = formset_factory(montaVetorCriterio, extra=int(qtdeCriterio))
            alternativaFormSet = formset_factory(montaVetorAlternativa, extra=int(qtdeAlternativa))
            pesoFormSet        = formset_factory(montaVetorPeso, extra=int(qtdeCriterio))
            return render(request, 'main/electreIII_indices_limites.html', {'criterioFormSet': criterioFormSet, 'alternativaFormSet' : alternativaFormSet, 'pesoFormSet' : pesoFormSet, 'alternativa' : qtdeAlternativa, 'criterio' : qtdeCriterio } )
        else:
            return render(request, 'main/electreIII_valores.html',{'form': form})
    else:
        return render(request, 'main/electreIII_valores.html',{'form': captura_entrada_form()})


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
    return render(request,'main/dados.html', {'alternativas': request.session['alternativa'],'tabela': tabela, 'criterios': request.session['criterio'], 'mDes': resultDes, 'mCon': resultCon, 'i': len(tabela[i])+1 , 'result': result, 'iT': len(tabela[i])+1 })

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_reader_electreIII(request)
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

    print result
    return render(request,'main/dados.html', {'alternativas': alternativa, 'criterios': criterios, 'tabela': tabela, 'mCon': mCon, 'i': len(tabela[i])+1 , 'result': result })

def csv_reader_electreIII(request):
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
        pesos.append(data[len(data)-4][i].replace(',','.'))
        criterios.append(data[0][i])
    for i in range(1,len(data)-2):
        linha=[]
        if i != 0 :
            for j in range(1,len(data[0])):
                linha.append(data[i][j])
            tabela.append(linha)
    c = float(data[len(data)-3][1].replace(',','.'))
    d = float(data[len(data)-3][2].replace(',','.'))
    p = float(data[len(data)-2][1].replace(',','.'))
    q = float(data[len(data)-2][2].replace(',','.'))
    v = float(data[len(data)-1][1].replace(',','.'))

    teste = len(tabela[0])
    mCon = matrizConcordanciaIII(alternativa, tabela, len(tabela), len(tabela[0]), pesos, p, q)
    mDes = matrizDiscordanciaIII(alternativa,tabela, len(tabela),  len(tabela[0]), pesos, p, v)
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

def matrizConcordanciaIII(cidades, tabela, nLinhas, nColunas, vetorPesos, p, q):

        somaPesos = 0
        mConcordancia = []
        for x in range(len(vetorPesos)):
            somaPesos += float(vetorPesos[x].replace(',','.'))
       
        for i in range(nColunas):
            linha = []
       
            for j in range(len(tabela[i])):
   
                somatorioW = 0
                for y in range(len(tabela[j])):
                    valor = 0
                    if float(tabela[i][y]) > (float(tabela[j][y]) - q):
                        valor = 1
                    else:
                        if float(tabela[i][y]) <= ((float(tabela[j][y]) - p)):
                            valor = 0
                        else:
                            somatorioW += float(vetorPesos[y]) * (p-(float(tabela[i][y])- float(tabela[j][y]))/p-q)
                    if valor == 1:
                        somatorioW += float(vetorPesos[y])
                result = 1.0/somaPesos * somatorioW
                linha.append(round(result, 2))
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
            linha.append(max(vetorIndices))
        mDiscordancia.append(linha)
    return mDiscordancia


def matrizDiscordanciaIII(cidades, tabela, nLinhas, nColunas, vetorPesos, p, v):


    matrizesDiscordancia = []

  
    for i in range(nColunas):
        mDiscordancia = []
  
        for j in range(len(tabela[i])):
            linha = []
       
            for y in range(len(tabela[j])):
                if i==y or j==y:
                    linha.append(0)
                else:
                    if float(tabela[i][y]) > (float(tabela[j][y]) - p):
                        linha.append(0)
                    else:
                        if float(tabela[i][y]) < (float(tabela[j][y]) - v):
                            linha.append(1)
                            
                        else:
                            result = ((float(tabela[i][y]) - float(tabela[j][y]) - p)/v-p)
                            linha.append(round(result, 2))
    
            mDiscordancia.append(linha)

        for x in range(len(mDiscordancia[j])):
            print mDiscordancia[x], cidades[x]

        matrizesDiscordancia.append(mDiscordancia)



    return matrizesDiscordancia


def matrizCredibilidade(cidades, nLinhas, nColunas, mConcordancia, mDiscordancia):
    print "\n\nMatriz de Credibilidade\n"

    matrizCredibilidade = []

    for i in range(nColunas):
        linha = []
        for j in range(len(mConcordancia[i])):
            indiceDiscordanciaMaior = False

            for k in range(nLinhas):
                if (mDiscordancia[k][i][j] > mConcordancia[i][j]):
                    indiceDiscordanciaMaior = True
            
            if (indiceDiscordanciaMaior):
                resultado1 = 1.0
                for k in range(nLinhas):
                    resultado1 *= round(((1.0-mDiscordancia[k][i][j])/(1.0-mConcordancia[i][j])), 2)
                resultado2 = mConcordancia[i][j] * resultado1
                
                linha.append(resultado2)
            else:
                linha.append(mConcordancia[i][j])
            
        matrizCredibilidade. append(linha)

    for x in range(nColunas):
        print matrizCredibilidade[x], cidades[x]

    return matrizCredibilidade

def destilacao(cidades, nColunas, nLinhas, mCredibilidade):


    destilacaoAscendente = []



    for i in range(len(mCredibilidade)):
        mCredibilidade[i].append(cidades[i])

    

    fim = False
    while (fim==False):

        

        lAst = lambdaAsterisco(lambdaMaxima(mCredibilidade, nColunas))

        vetorSelecionadas = determinaAlternativaAscendente(mCredibilidade, lAst, cidades)

        for k in range(len(vetorSelecionadas)):
            for i in range(len(mCredibilidade)):
                if (vetorSelecionadas[k][0] == mCredibilidade[i][len(mCredibilidade)]):
                    for j in range(len(mCredibilidade)):
                        for g in range(len(mCredibilidade)):
                            if (i == j or i == g):
                                mCredibilidade[j][g] = []




        zero = True
        for n in range(len(vetorSelecionadas)):
            if 0 != vetorSelecionadas[n][1]:
                zero = False
        if (zero):
            i = 0
            while (i < len(vetorSelecionadas)):
                achou = False
                for n in range(len(destilacaoAscendente)):
                    
                    if(vetorSelecionadas[i][0] == destilacaoAscendente[n][0]):
                        achou = True
                if (achou ==False):
                    destilacaoAscendente.append(vetorSelecionadas[i])
                i+=1
        else:
            for n in range(len(vetorSelecionadas)):
                destilacaoAscendente.append(vetorSelecionadas[n])

        fim = True
        for k in range(len(mCredibilidade)):
            for i in range(len(mCredibilidade)):
                if mCredibilidade[k][i] != []:
                    fim = False

    print destilacaoAscendente


def determinaAlternativaAscendente(mCredibilidade, lAst, cidades):


    matrizOrdenacao = []
    for i in range(len(mCredibilidade)):
        linha = []
        for j in range(len(mCredibilidade)):
                if (mCredibilidade[i][j] >= lAst) and mCredibilidade[i][j] != []:
                    linha.append(1)
                else:
                    linha.append(0)

        matrizOrdenacao.append(linha)
   
    matrizQualificacao = []
    for i in range(len(matrizOrdenacao)):
        vetorQualificacao = []
        valorLinha = 0
        valorColuna = 0
        for j in range(len(matrizOrdenacao)):
            for k in range(len(matrizOrdenacao[i])):
                if i == j:
                    valorLinha += matrizOrdenacao[j][k]
                if i == k:
                    valorColuna += matrizOrdenacao[j][k]
        resultado = valorLinha - valorColuna
        vetorQualificacao.append(cidades[i])
        vetorQualificacao.append(resultado)
        matrizQualificacao.append(vetorQualificacao)
    

    matrizQualificacao.sort(key=lambda x: x[1], reverse = True)

    vet = []
    for i in range(len(matrizOrdenacao)):
        vet.append(matrizQualificacao[i][1])

    maiorIndice = max(vet)

    altMaior = []
    for i in range(len(matrizOrdenacao)):
        if (matrizQualificacao[i][1] == maiorIndice):
            altMaior.append(matrizQualificacao[i])

    return altMaior


def lambdaMaxima(mCredibilidade, nAlternativas):

    lMax = 0
    for i in range(len(mCredibilidade)):
        for j in range(len(mCredibilidade)):
            if (i!=j) and (mCredibilidade[i][j] != []):
                if(mCredibilidade[i][j] > lMax):
                    lMax = mCredibilidade[i][j]
    #print lMax
    return lMax

def lambdaAsterisco(lMax):

    lAst = lMax - (0.3 - 0.15*lMax)

    return lAst



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
