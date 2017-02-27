from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.menu_principal),
    url(r'^main/base/$', views.insert_valores, name='insert_valores'),
    url(r'^main/resultado_matriz/$', views.resultado_matriz, name='resultado_matriz'),
    url(r'^main/sobre/$', views.sobre, name='sobre'),
    url(r'^ahp/ahp/$', views.ahp_insert_valores, name='ahp_insert_valores'),
    url(r'^ahp/focoprincipal/$', views.ahp_foco_principal, name='ahp_foco_principal'),
    url(r'^ahp/resultado/$', views.ahp_resultado, name='ahp_resultado'),
    url(r'^main/qtdeCriterioAlternativa/$', views.qtdeCriterioAlternativa, name='qtdeCriterioAlternativa'),
    url(r'^main/arquivo/$', views.upload_file, name='inserirArquivo'),
    url(r'^main/dados/$', views.csv_reader, name='dados'),
]
