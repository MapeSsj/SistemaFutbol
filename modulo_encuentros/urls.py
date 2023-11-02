from django.urls import path
from . import views

urlpatterns = [
    path('obtener-encuentros-no-jugados/', views.obtener_encuentros_no_jugados, name='obtener_encuentros_no_jugados'),
    path('obtener-jugadores-equipo/', views.obtener_encuentros_no_jugados, name='obtener_jugadores_equipo'),
    path('obtener-listado-jugadores/', views.obtener_listado_jugadores, name='obtener_listado_jugadores'),
    path('obtener-listado-jugadores-contratados-2/', views.obtener_listado_jugadores_contratados_2, name='obtener_listado_jugadores_contratados_2'),
    path('obtener-equipo-encuentro/', views.obtener_equipo_encuentro, name='obtener_equipo_encuentro'),
    path('agregar-convocatoria-equipos/', views.agregar_convocatoria_equipos, name='agregar_convocatoria_equipos'),
    path('lista_convocados/<int:convocatoria_id>/', views.lista_convocados_view, name='lista_convocados_view'),
    path('desconvocar/<int:jugador_id>/', views.desconvocar_jugador, name='desconvocar_jugador'),
    
    
    
    #path('obtener-jugadores-contratos/', views.obtener_jugadores_y_contratos, name='obtener_jugadores_y_contratos'),
    
    # Otras rutas específicas del módulo
]