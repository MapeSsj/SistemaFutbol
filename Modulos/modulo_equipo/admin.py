from django.contrib import admin
from django.utils.html import mark_safe 
from Modulos.modulo_equipo.models import*
# Register your models here.
@admin.register(categoria)
class categoria_admin(admin.ModelAdmin):
    list_display=('id','nombre','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones',)
    ordering=('id',)

#@admin.register(tipo_equipo)
class tipo_equipo_admin(admin.ModelAdmin):
    list_display=('id','descripcion','estado','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones',)
    ordering=('id',)

@admin.register(equipo)
class equipo_admin(admin.ModelAdmin):
    list_display=('id','nombre','siglas','categoria','tipo_equipo','sede','deporte','logo','vestimenta_principal','vestimenta_secundaria','portada','estado','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones',)
    ordering=('id',)


from django.urls import reverse
#Correguir con nuevas PLANTILLAS
@admin.register(convocatoria)
class convocatoria_admin(admin.ModelAdmin):
    change_form_template = 'detalle_convocatoria.html'
    list_display=('id','encuentro','equipo','fecha','btn_acceso_convocados',)
    
    ordering=('id',)
    
    def btn_acceso_convocados(self, obj):
        lista_convocados_url = reverse('lista_convocados_view', args=[obj.id])
        return mark_safe(f'<a href="{lista_convocados_url}"><b>Ver Jugadores</b></a>')
    btn_acceso_convocados.short_description = "Ver Jugadores"
    #####################################
    

#@admin.register(detalle_convocatoria)
##class detalle_convocatoria_admin(admin.ModelAdmin):
#    list_display=('id','jugador','btns_acciones')
#    def btns_acciones(self,obj):
#        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
#    btns_acciones.short_description = "Acciones"
#    list_display_links=('btns_acciones','id',)
#    ordering=('id',)


@admin.register(alineacion)
class alineacion_admin(admin.ModelAdmin):
    change_form_template = 'detalle_alineacion.html'
    list_display=('id','encuentro','formacion','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones','id')
    ordering=('id',)

#@admin.register(detalle_alineacion)
#class detalle_alineacion_admin(admin.ModelAdmin):
#    change_form_template = 'detalle_alineacion.html'
#    list_display=('id','equipo','juagador_c','titular','btns_acciones')
#    def btns_acciones(self,obj):
#        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
#    btns_acciones.short_description = "Acciones"
#    list_display_links=('btns_acciones','id')
#    ordering=('id',)

@admin.register(formacion)
class formacion_admin(admin.ModelAdmin):
    list_display=('id','descripcion','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div><b>Opciones Avanzadas</b></div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones','id')
    ordering=('id',)