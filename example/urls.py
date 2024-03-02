# example/urls.py
from django.urls import path

from example import views


urlpatterns = [
    path('', views.index),
    path('mapaCalculado/', views.calcularProduccionNecesaria, name='calcular_produccion'),
    path('produccion/<int:value>', views.userData),
    path('resourceNeedData/', views.resourceNeedData)
]