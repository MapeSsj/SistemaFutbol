from django.contrib import admin
from django.utils.html import mark_safe 
from Modulos.modulo_competicion.models import formato
from Modulos.modulo_competicion.models import*

from django.shortcuts import redirect,get_object_or_404
from django import forms
from django.contrib import messages

# Register your models here.
@admin.register(temporada)
class temporada_admin(admin.ModelAdmin):
    list_display=('id','nombre','modalidad','inicio','fin','estado','btns_acciones',)
    ordering=('id',)
    list_display_links=('btns_acciones',)
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"


@admin.register(pais)
class pais_admin(admin.ModelAdmin):
    list_display=('id','nombre','sigla','bandera','btns_acciones')
    ordering=('id',)
    list_display_links=('btns_acciones',)
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    
    

@admin.register(entidad)
class entidad_admin(admin.ModelAdmin):
    list_display=('id','pais','nombre','afileacion','sede','ambito','ubicado_en','estado','btns_acciones')
    ordering=('id',)
    list_display_links=('btns_acciones',)
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_filter=('pais','afileacion')
    search_fields=('pais','afileacion')

@admin.register(tipo_equipo)
class tipo_equipo_admin(admin.ModelAdmin):
    list_display=('id','descripcion','estado','btns_acciones')
    ordering=('id',)
    list_display_links=('btns_acciones',)
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    
@admin.register(tipo_competicion)
class tipo_competicion_admin(admin.ModelAdmin):
    list_display=('id','entidad','tipo_equipo','nombre','descripcion','estado','btns_acciones')
    ordering=('id',)
    list_display_links=('btns_acciones',)
    list_filter=('tipo_equipo','entidad',)
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    
@admin.register(formato)
class formato_admin(admin.ModelAdmin):
    list_display=(
        'id',
        'tipo_competicion',
        'temporada',
        'nombre',
        'cantidad_equipos',
        'cantidad_grupos',
        'tabla_acumulada',
        'cantidad_equipos_x_grupo',
        'fase_apertura',
        'fase_clausura',
        'cantidad_jornadas',
        'cantidad_equipos_clasificacion_directa',
        'cantidad_equipos_clasificacion_grupo',
        'play_off',
        'cantidad_equipos_clasificacion_fase_previa',
        'cantidad_etapas',
        'fase_grupos',
        'estado','btns_acciones')
    ordering=('id',)
    list_display_links=('btns_acciones','id','nombre','btns_acciones',)
    
    fieldsets=(
        (None,{
            'fields':('nombre',)
        }),
        ('ESTADO | DAR DE BAJA',{
            'classes':('collapse','wide','extrapretty'),
            'fields':('estado',)
        }),
        ('TODAS LAS OPCIONES',{
            'classes':('collapse','wide','extrapretty'),
            'fields':(
                'tipo_competicion',
                'temporada',
                'cantidad_equipos',
                'cantidad_jornadas',
                'tabla_acumulada',
                'fase_apertura',
                'fase_clausura',
                'fase_grupos',
                'play_off',
                'cantidad_grupos',
                'cantidad_equipos_x_grupo',    
                'cantidad_equipos_clasificacion_directa',
                'cantidad_equipos_clasificacion_grupo',
                'cantidad_equipos_clasificacion_fase_previa',
                'cantidad_etapas',
                'posicion_repesca',
                )
        })
    )
    list_filter=('temporada','tipo_competicion',)
    search_fields=('nombre',)
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['search_help_text'] = 'Ingresa el nombre del formato'
        return super().changelist_view(request, extra_context=extra_context)
    
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    

@admin.register(deporte)
class deporte_admin(admin.ModelAdmin):
    list_display=('id','nombre','estado','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('id','nombre','btns_acciones',)


@admin.register(competicion)
class competicion_admin(admin.ModelAdmin):
    search_fields=('nombre',)
    list_filter=('tipo_competicion','formato','temporada')
    list_display=(
        'id',
        'tipo_competicion',
        'formato',
        'temporada',
        'nombre',
        'estado',
        'btns_acciones'
        )
    ordering=('id',)
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('id','nombre','btns_acciones',)
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super().response_add(request, obj, post_url_continue)
        if "_addanother" not in request.POST and "_continue" not in request.POST:
            request.session['last_competicion_id'] = obj.id
            messages.add_message(request, messages.SUCCESS, 'Competición registrada con éxito.')
            return redirect('admin:modulo_competicion_pais_competicion_add')
        return response
    
#########################################################

        
@admin.register(pais_competicion)
class pais_competicion_admin(admin.ModelAdmin):
    list_display=('pais','competicion',)
    list_filter=('pais','competicion',)
    
    
##################################

@admin.register(patrocinador)
class PatrocinadorAdmin(admin.ModelAdmin):
    list_display = ('id','competicion','nombre_oficial','nombre_corto','logo1','estado','btns_acciones')
    search_fields=('nombre_oficial','competicion',)
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones',)
    list_filter=('competicion',)
    ordering=('id',)

@admin.register(grupo)
class grupo_admin(admin.ModelAdmin):
    list_display=('id','nombre','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('id','btns_acciones')
    ordering=('id',)

@admin.register(fase)
class admin_fase(admin.ModelAdmin):
    list_display=('id','nombre','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"


@admin.register(detalle_grupo_competicion)
class detalle_grupo_competicion_admin(admin.ModelAdmin):
    list_display=('id','competicion','equipo')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_filter=('competicion',)

@admin.register(jornada)
class jornada(admin.ModelAdmin):
    list_display=('id','nombre',)