from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro_mongo', views.registro_mongo, name='registro_mongo'),
    path('ponto_redis', views.ponto_redis),
    
]

