from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse
from .models import formacion,posicion_jugador
#from modulo_contrato.models import persona
from Modulos.modulo_contrato.models import contrato,persona
from Modulos.modulo_encuentros.models import encuentro
import json

def obtener_formacion(request):
    formaciones = list(formacion.objects.all().values('id', 'descripcion'))
    data = json.dumps(formaciones)
    return HttpResponse(data, content_type='application/json')

def obtener_posicion_jugador(request):
    posiciones = list(posicion_jugador.objects.all().values('id', 'descripcion'))
    data = json.dumps(posiciones)
    return HttpResponse(data, content_type='application/json')


def obtener_jugadores_equipo(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'GET':
        encuentro_id = request.GET.get('encuentro_id')
        
        # Obtiene el encuentro seleccionado
        encuentro_obj = encuentro.objects.get(pk=encuentro_id)
        
        # Obtiene los jugadores de los equipos locales y visitantes
        jugadores_equipo_local = contrato.objects.filter(nuevo_club=encuentro_obj.equipo_local)
        jugadores_equipo_visitante = contrato.objects.filter(nuevo_club=encuentro_obj.equipo_vistante)
        
        # Construye una lista de jugadores para cada equipo
        jugadores_equipo_local_list = [{'id': jugador.id, 'nombre': jugador.persona.nombres} for jugador in jugadores_equipo_local]
        jugadores_equipo_visitante_list = [{'id': jugador.id, 'nombre': jugador.persona.nombres} for jugador in jugadores_equipo_visitante]
        
        return JsonResponse({'equipoLocal': jugadores_equipo_local_list, 'equipoVisitante': jugadores_equipo_visitante_list})
    
    return JsonResponse({'error': 'No es una solicitud AJAX válida :('})

