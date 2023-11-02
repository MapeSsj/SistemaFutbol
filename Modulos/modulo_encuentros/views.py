from django.shortcuts import render
from django.http import JsonResponse
from .models import encuentro
# Create your views here.
from Modulos.modulo_contrato.models import persona
from Modulos.modulo_contrato.models import contrato
from Modulos.modulo_equipo.models import equipo
from .models import encuentro
from Modulos.modulo_equipo.models import convocatoria,detalle_convocatoria

def obtener_encuentros_no_jugados(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'GET':
        competicion_id = request.GET.get('competicion_id')
        # Filtra los encuentros no jugados de la competición seleccionada
        encuentros = encuentro.objects.filter(competicion=competicion_id, estado_jugado=False)
        # Construye una lista de encuentros en el formato "equipo_local vs equipo_vistante"
        encuentros_list = [f"{encuentro.equipo_local} vs {encuentro.equipo_vistante} ({encuentro.jornada})" for encuentro in encuentros]
        return JsonResponse(encuentros_list, safe=False)
    return JsonResponse({'error': 'No es una solicitud AJAX válida'})



def obtener_jugadores_equipo(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'GET':
        encuentro_id = request.GET.get('encuentro_id')
        
        # Obtiene el encuentro seleccionado
        encuentro_obj = encuentro.objects.get(pk=encuentro_id)
        jugadores=list(persona.objects.all().values('id','nombres'))
        # Obtiene los jugadores de los equipos locales y visitantes
        jugadores_equipo_local = contrato.objects.filter(nuevo_club=encuentro_obj.equipo_local)
        jugadores_equipo_visitante = contrato.objects.filter(nuevo_club=encuentro_obj.equipo_vistante)
        
        # Construye una lista de jugadores para cada equipo
        #jugadores_equipo_local_list = [{'id': jugador.id, 'nombre': jugador.persona.nombres} for jugador in jugadores_equipo_local]
        jugadores_equipo_local_list = [{'id': jugador.id, 'nombre': jugador.persona.nombres} for jugador in jugadores_equipo_local]
        jugadores_list = [{'id': jugador.id, 'nombre': f"{jugador.nombres} {jugador.apellidos}"} for jugador in jugadores]


        
        print(jugadores_list)
        return JsonResponse({'equipoLocal': jugadores_list, 'equipoVisitante': jugadores_list})
    
    return JsonResponse({'error': 'No es una solicitud AJAX válida :('})

def obtener_listado_jugadores(request):
    jugadores = list(persona.objects.all().values('id', 'nombres', 'apellidos', 'alias', 'sexo', 'fecha_nacimiento', 'estatura', 'peso', 'foto', 'estado'))    
    return JsonResponse(jugadores, safe=False)


##################
from django.http import JsonResponse

def obtener_listado_jugadores_contratados_2(request):
    
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'GET':
        equipo_id = request.GET.get('equipo_id')
        try:
            equipo_obj = equipo.objects.get(pk=equipo_id)
            contratos = contrato.objects.filter(nuevo_club=equipo_obj)
            jugadores = [contrato.persona for contrato in contratos]

            # Convierte los datos a un formato JSON y devuélvelos como una respuesta JSON.
            data = [{'id': jugador.id, 'nombres': jugador.nombres, 'apellidos': jugador.apellidos, 'alias': jugador.alias, 'sexo': jugador.sexo, 'fecha_nacimiento': jugador.fecha_nacimiento, 'estatura': jugador.estatura, 'peso': jugador.peso, 'foto': jugador.foto.url if jugador.foto else None, 'estado': jugador.estado} for jugador in jugadores]
            return JsonResponse(data, safe=False)
        except equipo.DoesNotExist:
            return JsonResponse({'error': 'El equipo no existe.'}, status=404)


def obtener_equipo_encuentro(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'GET':
        encuentro_id = request.GET.get('encuentro_id')
        try:
            encuentro_obj = encuentro.objects.get(pk=encuentro_id)

            # Aquí asumimos que en tu modelo de Encuentro tienes dos campos ForeignKey, uno para el equipo local y otro para el equipo visitante.
            equipo_local_ = encuentro_obj.equipo_local
            equipo_visitante_ = encuentro_obj.equipo_vistante

            # Ahora puedes acceder a los datos de los equipos, por ejemplo:
            nombre_equipo_local = equipo_local_.nombre
            nombre_equipo_visitante = equipo_visitante_.nombre
            
            id_local=equipo_local_.id
            id_visita=equipo_visitante_.id

            # Luego, puedes devolver los datos de los equipos como una respuesta JSON.
            return JsonResponse({
                'equipo_local': nombre_equipo_local,
                'id_equipo_loca':id_local,
                'equipo_visitante': nombre_equipo_visitante,
                'id_equipo_visita':id_visita,
            })
        except encuentro.DoesNotExist:
            return JsonResponse({'error': 'El encuentro no existe.'}, status=404)


from django.http import HttpResponseRedirect
from django.urls import reverse 
def agregar_convocatoria_equipos(request):
    if request.method == 'POST':
        jugadores_seleccionados_elocal = request.POST.getlist('jugadoresSeleccionadosLocal[]')
        jugadores_seleccionados_evisita = request.POST.getlist('jugadoresSeleccionadosVisita[]')
        
        encuentro_seleccionado = request.POST.get('encuentroSeleccionado')
        
        id_local = request.POST.get('idLocal')  # Accede al ID de equipo local
        id_visita = request.POST.get('idVisita')  # Accede al ID de equipo visita
        
        nueva_convocatoria_l = convocatoria.objects.create(encuentro_id=encuentro_seleccionado, equipo_id=id_local)
        nueva_convocatoria_v = convocatoria.objects.create(encuentro_id=encuentro_seleccionado, equipo_id=id_visita)
        
        # Ejemplo: crea detalles de convocatoria para los jugadores seleccionados
        for jugador_id in jugadores_seleccionados_elocal:
            detalle = detalle_convocatoria(jugador_id=jugador_id, convocatoria=nueva_convocatoria_l)
            detalle.save()
        
        for jugador_id in jugadores_seleccionados_evisita:
            detalle = detalle_convocatoria(jugador_id=jugador_id, convocatoria=nueva_convocatoria_v)
            detalle.save()
        
        # Si todo salió bien, puedes devolver una respuesta de éxito
        return HttpResponseRedirect(reverse('admin:modulo_equipo_convocatoria_changelist'))


    # Si la solicitud no es POST o algo salió mal, devuelve una respuesta de error
    return JsonResponse({'success': False})







def lista_convocados_view(request, convocatoria_id):
    
    # Utiliza filter() para obtener una lista de jugadores convocados en la convocatoria específica
    jugadores_convocados = detalle_convocatoria.objects.filter(convocatoria_id=convocatoria_id)
    convocatoria_ = convocatoria.objects.get(pk=convocatoria_id)
    # Luego, obtén la lista de personas (jugadores) basándote en la lista de jugadores convocados
    jugadores = persona.objects.filter(id__in=jugadores_convocados.values('jugador_id'))
    return render(request, 'lista_convocados.html', {'convocatoria':convocatoria_,'jugadores_convocados': jugadores_convocados})


from django.shortcuts import get_object_or_404, redirect
def desconvocar_jugador(request, jugador_id):
    jugador_convocado = get_object_or_404(detalle_convocatoria, id=jugador_id)
    # Elimina el jugador convocado de la base de datos
    jugador_convocado.delete()
    return redirect(request.META.get('HTTP_REFERER'))

