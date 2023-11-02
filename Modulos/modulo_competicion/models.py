from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save



# Create your models here.
# TEMPORADA -> 
class temporada(models.Model):
    class Meta:
        verbose_name = "temporada".upper()
        verbose_name_plural = "temporadas".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    modalidad_lis = [
    ("EUROPEA", "EUROPEA"),
    ("LIGA", "LIGA"),
    ("Copa de Europa (UEFA Champions League)", "Copa de Europa (UEFA Champions League)"),
    ("TORNEO", "TORNEO"),
    ("COPA PAIS", "COPA PAIS"),
    ("SELECCIONES", "SELECCIONES"),
    ]
    modalidad=models.CharField(max_length=100, choices=modalidad_lis)
    inicio=models.DateField()
    fin=models.DateField()
    estado=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return format(self.nombre)

class pais(models.Model):
    class Meta:
        verbose_name = "pais".upper()
        verbose_name_plural = "paises".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    sigla=models.CharField(max_length=3)
    bandera=models.ImageField(blank=True,null=True,upload_to='bandera/',default='bandera/bandera_default.png')
    
    
    def __str__(self):
        txt="{0} ({1})"
        return txt.format(self.nombre,self.sigla)

class entidad(models.Model):
    class Meta:
        verbose_name = "entidad".upper()
        verbose_name_plural = "entidades".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    pais=models.ForeignKey(pais,null=False,blank=False,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50)
    afileacion=models.CharField(max_length=100)
    sede=models.CharField(max_length=100)
    ambito =models.CharField(choices=[("Fútbol","Fútbol")],max_length=30)
    ubicado_en=models.TextField()
    estado=models.BooleanField(default=True)    
    
    def __str__(self):
        return format(self.nombre)
    

class tipo_equipo(models.Model):
    class Meta:
        verbose_name = "tipo de equipo".upper()
        verbose_name_plural = "tipo de equipos".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=40)
    estado=models.BooleanField(default=True)
    
    def __str__(self):
        return format(self.descripcion)

class tipo_competicion(models.Model):
    class Meta:
        verbose_name = "tipo de competicion".upper()
        verbose_name_plural = "tipo de competiciones".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    entidad=models.ForeignKey(entidad,null=False,blank=False,on_delete=models.CASCADE)
    tipo_equipo=models.ForeignKey(tipo_equipo,null=False,blank=False,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=150)
    descripcion=models.TextField(blank=True,null=True)
    estado=models.BooleanField(default=True) 
    
    def __str__(self):
        txt=("{0} ({1})")
        return txt.format(self.nombre,self.entidad)

class formato(models.Model):
    class Meta:
        verbose_name = "formato".upper()
        verbose_name_plural = "formatos".upper()
    #############################################
    id = models.AutoField(primary_key=True)
    tipo_competicion = models.ForeignKey(tipo_competicion, null=False, blank=False, on_delete=models.CASCADE)
    temporada = models.ForeignKey(temporada, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    cantidad_equipos = models.PositiveSmallIntegerField(default=0)
    cantidad_grupos = models.PositiveSmallIntegerField(default=0)
    tabla_acumulada = models.BooleanField(default=False)
    cantidad_equipos_x_grupo = models.PositiveSmallIntegerField(default=1)
    fase_apertura = models.BooleanField(default=False)
    fase_clausura = models.BooleanField(default=False)
    fase_grupos = models.BooleanField(default=False)
    play_off = models.BooleanField(default=False)
    cantidad_jornadas = models.PositiveSmallIntegerField(default=0)
    cantidad_equipos_clasificacion_directa = models.PositiveSmallIntegerField(default=0)
    cantidad_equipos_clasificacion_grupo = models.PositiveSmallIntegerField(default=0)

    def posicion_repesca_choices(self):
        lista = [(i, i) for i in range(1, self.cantidad_equipos + 1)]
        return lista

    
    cantidad_equipos_clasificacion_fase_previa = models.PositiveSmallIntegerField(default=0)

    tuppla_fases_grupos = [
        (0,"NO TIENE"),
        (6, "32avos de Final "),
        (5, "16avos de Final"),
        (4, "8avos de Final"),
        (3, "4tos de Final "),
        (2, "Semifinal"),
        (1, "Final")
    ]
    
    cantidad_etapas = models.IntegerField(choices=tuppla_fases_grupos,default=0)
    posicion_repesca=models.PositiveSmallIntegerField(default=0)
    
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class deporte(models.Model):
    class Meta:
        verbose_name = "deporte".upper()
        verbose_name_plural = "deportes".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(blank=False,max_length=30)
    estado=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return format(self.nombre)
    
    
    
class competicion(models.Model):
    class Meta:
        verbose_name = "competicion".upper()
        verbose_name_plural = "competiciones".upper()
    #############################################
    
    id=models.AutoField(primary_key=True)
    deporte=models.ForeignKey(deporte,blank=False,null=False,on_delete=models.CASCADE)
    tipo_competicion=models.ForeignKey(tipo_competicion,blank=False,null=False,on_delete=models.CASCADE)
    formato=models.ForeignKey(formato,blank=False,null=False,on_delete=models.CASCADE)
    temporada=models.ForeignKey(temporada,blank=False,null=False,on_delete=models.CASCADE)
    nombre=models.CharField(blank=False,max_length=100,null=False)
    fecha_inicio=models.DateField(blank=True, null=True)
    fecha_fin=models.DateField(null=True,blank=True)
    estado=models.BooleanField(default=True)
    paises = models.ManyToManyField('Pais', through='pais_competicion')
    def __str__(self) -> str:
        return format(self.nombre)
    
#participacion donde se juega la competicion
class pais_competicion(models.Model):
    class Meta:
        verbose_name = "Pais Asignados a Competiciones de Futbol".upper()
        verbose_name_plural = "Paises Asignados a Competiciones de Futbol".upper()
    #############################################
    pais = models.ForeignKey(pais, on_delete=models.CASCADE)
    competicion = models.ForeignKey(competicion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pais} - {self.competicion}"


class patrocinador(models.Model):
    class Meta:
        verbose_name = "PATROCINADOR".upper()
        verbose_name_plural = "PATROCINADORES".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    competicion=models.ForeignKey(competicion,blank=False,null=False,on_delete=models.CASCADE)
    nombre_oficial=models.CharField(max_length=70)
    nombre_corto=models.CharField(max_length=40)
    abreviatura=models.CharField(max_length=8)
    logo1=models.ImageField(blank=True,null=True,upload_to='patrocinador/',default='patrocinador/patrocinador_default.png')
    logo2=models.ImageField(blank=True,null=True,upload_to='patrocinador/',default='patrocinador/patrocinador_default.png')
    logo3=models.ImageField(blank=True,null=True,upload_to='patrocinador/',default='patrocinador/patrocinador_default.png')
    estado=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return format(self.nombre_oficial)
    
class jornada(models.Model):
    class Meta:
        verbose_name = "jornada".upper()
        verbose_name_plural = "jornadas".upper()
    #############################################
    
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,blank=False,null=False)
    def __str__(self) -> str:
        return format(self.nombre)
    
class fase(models.Model):
    class Meta:
        verbose_name = "Fase".upper()
        verbose_name_plural = "fases".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return format(self.nombre)

class grupo(models.Model):
    class Meta:
        verbose_name = "grupo".upper()
        verbose_name_plural = "grupos".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return format(self.nombre)



class detalle_grupo_competicion(models.Model):
    class Meta:
        verbose_name = "Equipo que Pertenen a un Competicion".upper()
        verbose_name_plural = "Equipos que Pertenen a Competiciones".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    competicion=models.ForeignKey(competicion,blank=False,null=False,on_delete=models.CASCADE,default=1)
    fase=models.ForeignKey(fase,blank=True,null=True,on_delete=models.CASCADE,default=1)
    grupo=models.ForeignKey(grupo,blank=True,null=True,on_delete=models.CASCADE,default=1)
    equipo=models.ForeignKey('modulo_equipo.equipo',blank=False,null=False,on_delete=models.CASCADE,default=1)
    
    
    
    