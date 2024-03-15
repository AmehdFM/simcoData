# example/urls.py
from django.urls import path

from example import views


urlpatterns = [
    #API?
    path('api/BuildingResourcesCalculator/', views.BuildingResourcesCalculator),

    path('', views.index),


    path('elegirRecurso/', views.elegirRecurso),
    path('mapaCalculado/', views.calcularProduccionNecesaria, name='calcular_produccion'),
    path('produccion/<int:value>', views.userData),
    path('resourceNeedData/', views.resourceNeedData),
    path('constructionCalculator/', views.buildingPage),

]