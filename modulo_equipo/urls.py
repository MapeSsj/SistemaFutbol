from django.urls import path
from . import views

urlpatterns = [
    path('obtener-formacion/', views.obtener_formacion, name='obtener_formacion'),
    path('obtener-posicion-jugador/', views.obtener_posicion_jugador, name='obtener_posicion_jugador'),
    path('obtener-jugadores/', views.obtener_jugadores_equipo, name='obtener_jugadores_equipo'),
    
    # Otras rutas específicas del módulo
]