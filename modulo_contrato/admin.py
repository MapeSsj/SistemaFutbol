from django.contrib import admin
from Modulos.modulo_contrato.models import*
from django.utils.html import mark_safe 

# Register your models here.
@admin.register(tipo_persona)
class tipo_persona_admin(admin.ModelAdmin):
    list_display=('id','descripcion','estado','btns_acciones')
    search_fields=('descripcion',)
    def btns_acciones(self,obj):
        return mark_safe('<div>Opciones Avanzadas</div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('btns_acciones','id','descripcion')
    list_per_page=(10)
    
@admin.register(persona)
class persona_admin(admin.ModelAdmin):
    list_display=('id','nombres','apellidos','tipo_persona','alias','sexo','foto','estado','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div>Opciones Avanzadas</div>')
    btns_acciones.short_description = "Acciones"
    list_display_links=('nombres','id','btns_acciones')
    search_fields=('nombres','apellidos')
    list_filter=('tipo_persona',)
    list_per_page=(10)
    
@admin.register(contrato)
class contrato_admin(admin.ModelAdmin):
    list_display=('id','persona','tipo_contrato','nuevo_club','ultimo_club','valor','fecha_inicio','fecha_fin','dorsal','posicion','estado','btns_acciones')
    def btns_acciones(self,obj):
        return mark_safe('<div>Opciones Avanzadas</div>')
    btns_acciones.short_description = "Acciones"
    list_filter=('tipo_contrato',)
    ordering=('id',)
    list_display_links=('id','persona','btns_acciones',)
    list_per_page=(10)
