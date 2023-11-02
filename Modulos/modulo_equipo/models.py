from django.db import models

# Create your models here.
class categoria(models.Model):
    class Meta:
        verbose_name = "Categoria".upper()
        verbose_name_plural = "Categorias".upper()
    #############################################
    
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(blank=False,null=False,max_length=50)
    def __str__(self) -> str:
        return format(self.nombre.upper())
    
class tipo_equipo(models.Model):
    class Meta:
        verbose_name = "Tipo de Equipo".upper()
        verbose_name_plural = "Tipo de Equipos".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(blank=False,null=False,max_length=30)
    estado=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return format(self.descripcion)
    
class equipo(models.Model):
    class Meta:
        verbose_name = "equipo".upper()
        verbose_name_plural = "Equipos".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,default='')
    siglas=models.CharField(max_length=3)
    presidente=models.CharField (max_length=100)
    categoria=models.ForeignKey(categoria,blank=False,null=False,on_delete=models.CASCADE)
    tipo_equipo=models.ForeignKey(tipo_equipo,blank=True,null=True,on_delete=models.CASCADE)
    sede=models.ForeignKey('modulo_encuentros.sede',blank=False,null=False,on_delete=models.CASCADE)
    deporte=models.ForeignKey('modulo_competicion.deporte',blank=False,null=False,on_delete=models.CASCADE)
    logo=models.ImageField(null=True, blank=True, upload_to='equipo/vestimenta_principal/')
    vestimenta_principal=models.ImageField(null=True, blank=True, upload_to='equipo/vestimenta_principal/')
    vestimenta_secundaria=models.ImageField(null=True,blank=True, upload_to='equipo/vestimenta_secundaria/')
    portada=models.ImageField(null=True,blank=True,upload_to='equipo/portada/')
    estado=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return format(self.nombre)


class formacion(models.Model):
    class Meta:
        verbose_name = "formacion".upper()
        verbose_name_plural = "formacion".upper()
    ###############################################
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=20)

    def __str__(self) -> str:
        return format(self.descripcion)

class posicion_jugador(models.Model):
    class Meta:
        verbose_name = "Posicion Jugador".upper()
        verbose_name_plural = "Posicion Jugador".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)

from django.utils import timezone
class convocatoria(models.Model):
    class Meta:
        verbose_name = "Convocatoria".upper()
        verbose_name_plural = "Convocatorias".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    encuentro=models.ForeignKey('modulo_encuentros.encuentro',null=False,blank=False,on_delete=models.CASCADE)
    equipo=models.ForeignKey(equipo,null=False,blank=False,on_delete=models.CASCADE)
    fecha=models.DateField(default=timezone.now,blank=True,null=True)
    
    def __str__(self) -> str:
        return format(self.equipo)
    

class detalle_convocatoria(models.Model):
    class Meta:
        verbose_name = "Detalle de Convocatoria".upper()
        verbose_name_plural = "Detalles de Convocatoria".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    jugador=models.ForeignKey('modulo_contrato.persona',blank=False,null=False,on_delete=models.CASCADE)
    convocatoria=models.ForeignKey(convocatoria,null=False,blank=False,on_delete=models.CASCADE)
    #activo=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        txt=("{0} ({1})")
        return txt.format(self.jugador,self.convocatoria)
    
class alineacion(models.Model):
    class Meta:
        verbose_name = "Alineacion".upper()
        verbose_name_plural = "Alineaciones".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    encuentro=models.ForeignKey('modulo_encuentros.encuentro',null=False,blank=False,on_delete=models.CASCADE)
    formacion=models.ForeignKey(formacion,blank=False,null=False,on_delete=models.CASCADE)
    confirmada=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        txt=("Alineacion de {0}")
        return txt.format(self.encuentro)
    
class detalle_alineacion(models.Model):
    class Meta:
        verbose_name = "Alieneacion Equipo".upper()
        verbose_name_plural = "Alineaciones de Equipos".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    equipo=models.ForeignKey('modulo_equipo.equipo',null=False,blank=False,on_delete=models.CASCADE)
    alineacion=models.ForeignKey(alineacion,blank=False,null=False,on_delete=models.CASCADE)
    posicion_jugador=models.ForeignKey(detalle_convocatoria,blank=False,null=False,on_delete=models.CASCADE)
    juagador_c=models.ForeignKey('modulo_contrato.contrato',null=False,blank=False,on_delete=models.CASCADE)
    ###########################
    dorsal=models.IntegerField()
    capitan=models.BooleanField(default=False)
    titular=models.BooleanField(default=False)
    
    def __str__(self):
        txt=("{0} - {1} ({3})")
        return txt.format(self.equipo,self.juagador_C,self.dorsal)
    
    
    
