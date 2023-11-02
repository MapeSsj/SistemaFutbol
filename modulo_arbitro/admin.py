from django.contrib import admin
from Modulos.modulo_arbitro.models import *
from django.utils.html import mark_safe


# Register your models here.
@admin.register(arbitro)
class arbitro_admin(admin.ModelAdmin):
    search_fields=('id','nombres',)
    list_display=('id','nombres','apellidos','fecha_nacimiento','tipo_arbitro','pais','estado','btns_acciones')
    list_display_links=('btns_acciones',)
    def btns_acciones(self,obj):
        return mark_safe('<div>Opciones Avanzadas</div>')
    btns_acciones.short_description = "Acciones"

@admin.register(tipo_terna)
class tipo_terna_admin(admin.ModelAdmin):
    list_display=('id','descripcion','sigla','btns_acciones')
    list_display_links=('btns_acciones',)
    search_fields=('id','descripcion',)
    ordering=('id',)
    def btns_acciones(self,obj):
        return mark_safe('<div>Opciones Avanzadas</div>')
    btns_acciones.short_description = "Acciones"

@admin.register(terna_arbitral)
class terna_arbitral_admin(admin.ModelAdmin):
    list_display=('id','nombre','estado','btns_acciones')
    list_display_links=('btns_acciones',)
    search_fields=('id','descripcion',)
    
    def btns_acciones(self,obj):
        return mark_safe('<div>Opciones Avanzadas</div>')
    btns_acciones.short_description = "Acciones"

@admin.register(detalle_terna)
class detalle_terna_admin(admin.ModelAdmin):
    list_display=('id','terna_arbitral','arbitro','tipo_terna','estado_juego','btns_acciones',)
    
    list_display_links=('btns_acciones',)
    def btns_acciones(self,obj):
        return mark_safe('<div>Opciones Avanzadas</div>')
    btns_acciones.short_description = "Acciones"
    
##############################################
    
