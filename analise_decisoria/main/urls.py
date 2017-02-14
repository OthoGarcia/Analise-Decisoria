from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.menu_principal),
    url(r'^main/base/$', views.insert_valores, name='insert_valores'),
    url(r'^main/resultado_matriz/$', views.resultado_matriz, name='resultado_matriz'),
    url(r'^main/sobre/$', views.sobre, name='sobre'),
    url(r'^ahp/ahp/$', views.ahp_insert_valores, name='ahp_insert_valores'),
]
