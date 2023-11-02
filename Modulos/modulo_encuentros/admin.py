from django.contrib import admin
from Modulos.modulo_encuentros.models import*
from django.utils.html import mark_safe 
# Register your models here.

@admin.register(ciudad)
class ciudad_admin(admin.ModelAdmin):
    list_display=('id','nombre','pais','norma','btns_acciones')
    
    list_display_links=('btns_acciones','id','nombre')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    
    list_filter=('pais',)

@admin.register(sede)
class sede_admin(admin.ModelAdmin):
    list_display=('id','nombre','alias','ciudad','capacidad','fecha_inaguracion','estado','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones',)
    list_filter=('ciudad',)
    
@admin.register(evento)
class evento_admin(admin.ModelAdmin):
    list_display=('id','descripcion','estado','btns_acciones')
    
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones',)

@admin.register(tipo_lesion)
class tipo_lesion_admin(admin.ModelAdmin):
    list_display=('id','nombre','descripcion','btns_acciones')
    
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones',)

@admin.register(evento_persona)
class evento_persona_admin(admin.ModelAdmin):
    list_display=('id','persona','encuentro','evento',)

@admin.register(encuentro)
class encuentro_admin2(admin.ModelAdmin):
    list_display=(
        'id',
        'competicion',
        'jornada',
        'equipo_local',
        'equipo_vistante',
        'resultado_local',
        'resultado_local',
        'resultado_goles_local',
        'resultado_goles_visita',
        'estado_jugado',
        'btns_acciones',)
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones',)