from django.urls import path
from . import views

urlpatterns = [
    path('obtener-competiciones/', views.obtener_competiciones, name='obtener_competiciones'),
    # Otras rutas específicas del módulo
]