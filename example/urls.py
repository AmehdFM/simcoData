# example/urls.py
from django.urls import path

from example import views


urlpatterns = [
    path('', views.mapaDistribucion),
    path('calcular/', views.calcular, name='calcular'),
    path('mapaCalculado/', views.calcularProduccionNecesaria, name='calcular_produccion'),
]