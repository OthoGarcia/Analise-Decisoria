from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.menu_principal),
    url(r'^main/base/$', views.insert_valores, name='insert_valores'),
    url(r'^main/resultado_matriz/$', views.resultado_matriz, name='resultado_matriz'),
]
