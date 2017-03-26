from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.menu_principal),
    url(r'^main/base/$', views.insert_valores, name='insert_valores'),
    url(r'^main/resultado_matriz/$', views.resultado_matriz, name='resultado_matriz'),
    url(r'^main/sobre/$', views.sobre, name='sobre'),
    url(r'^ahp/ahp/$', views.ahp_insert_valores, name='ahp_insert_valores'),
    url(r'^ahp/informaCriterioAlternativa/$', views.ahp_informaCriterioAlternativa, name='ahp_informaCriterioAlternativa'),
    url(r'^ahp/resultado/$', views.ahp_resultado, name='ahp_resultado'),
    url(r'^ahp/teste/$', views.teste, name='teste'),
    url(r'^main/qtdeCriterioAlternativa/$', views.qtdeCriterioAlternativa, name='qtdeCriterioAlternativa'),
    url(r'^main/arquivo/$', views.upload_file, name='inserirArquivo'),
    url(r'^main/dados/$', views.csv_reader, name='dados'),
    url(r'^main/alternativas/$', views.getAlternativas, name='getAlternativas'),
    url(r'^main/alternativasIII/$', views.getAlternativasIII, name='getAlternativasIII'),
    url(r'^main/electreIII_InformaIndice/$', views.electreIII_InformaIndice, name='electreIII_InformaIndice'),
    url(r'^main/preencheMatriz/$', views.preencheMatriz, name='preencheMatriz'),
    url(r'^main/preencheMatrizIII/$', views.preencheMatrizIII, name='preencheMatrizIII'),
    url(r'^main/electreIII/$', views.electreIII, name='electreIII'),
    url(r'^main/electreTri/$', views.electreTri, name='electreTri'),
    url(r'^main/electreTri_InformaCriterioAlternativa/$', views.getAlternativasTri, name='getAlternativasTri'),
    url(r'^main/electreTri_InformaIndice/$', views.electreTri_InformaIndice, name='electreTri_InformaIndice'),
    url(r'^main/electreIII_valores/$', views.electreIII_valores, name='electreIII_valores'),
]
