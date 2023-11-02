from django.db import models

# Create your models here.
class ciudad(models.Model):
    class Meta:
        verbose_name = "ciudad".upper()
        verbose_name_plural = "ciudades".upper()

    id=models.AutoField(primary_key=True)
    pais=models.ForeignKey('modulo_competicion.pais',blank=False,null=False,on_delete=models.CASCADE)
    nombre=models.CharField(blank=False,null=False,max_length=100)
    norma=models.CharField(max_length=3)
    
    def __str__(self) -> str:
        txt=("{0} ({1})")
        return txt.format(self.nombre,self.pais)

class sede(models.Model):
    class Meta:
        verbose_name = "sede".upper()
        verbose_name_plural = "sedes".upper()
    ###############################################
    id=models.AutoField(primary_key=True)
    ciudad=models.ForeignKey(ciudad,blank=False,null=False,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=255)
    alias=models.CharField(max_length=100, null=True,blank=True)
    capacidad=models.PositiveSmallIntegerField(default=0)
    fecha_inaguracion=models.DateField()
    list_estado=[
        ('SD','SUSPENDIDO DEFINITIVAMENTE'),
        ('DI','DISPONIBLE'),
        ('EM','EN MANTENIMIENTO'),
        ('ND','NO DISPONIBLE'),
        ('ST','SUSPENDIDO TEMPORALMENTE')
    ]
    estado=models.CharField(choices=list_estado,max_length=2)
    
    def __str__(self) -> str:
        return format(self.nombre)
    


    

class encuentro(models.Model):
    class Meta:
        verbose_name = "encuentro".upper()
        verbose_name_plural = "encuentros".upper()
    ###############################################
    id=models.AutoField(primary_key=True)
    competicion=models.ForeignKey('modulo_competicion.competicion',blank=False,null=False,on_delete=models.CASCADE)
    sede=models.ForeignKey(sede,blank=True,null=True,on_delete=models.CASCADE)
    terna_arbitral=models.ForeignKey('modulo_arbitro.terna_arbitral',null=True,blank=True,on_delete=models.CASCADE)
    equipo_local=models.ForeignKey('modulo_equipo.equipo',blank=False,null=False,on_delete=models.CASCADE, related_name='e_local')
    equipo_vistante=models.ForeignKey('modulo_equipo.equipo',blank=False,null=False,on_delete=models.CASCADE,related_name='e_visita')
    jornada=models.ForeignKey('modulo_competicion.jornada',blank=False,null=False,on_delete=models.CASCADE)
    list_resultado=[
        ('-','-'),
        ('G', 'GANADO'),
        ('E', 'EMPATADO'),
        ('P', 'PERDIDO'),
    ]
    resultado_local=models.CharField(max_length=1,choices=list_resultado,default='-')
    resultado_visita=models.CharField(max_length=1,choices=list_resultado,default='-')
    ####
    resultado_goles_local=models.PositiveSmallIntegerField(null=True,blank=True)
    resultado_goles_visita=models.PositiveSmallIntegerField(null=True,blank=True)
    ##
    fecha=models.DateField()
    hora=models.TimeField(null=True,blank=True)
    humedad=models.CharField(max_length=4,null=True,blank=True)
    clima=models.CharField(max_length=4,null=True,blank=True)
    estado_jugado=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        txt=("{0} VS {1}")
        return txt.format(self.equipo_local,self.equipo_vistante)
    

class evento(models.Model):
    class Meta:
        verbose_name = "evento".upper()
        verbose_name_plural = "eventos".upper()
    ###############################################
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=50)
    estado=models.BooleanField(default=True)

    def __str__(self) -> str:
        return format(self.descripcion)

class tipo_lesion(models.Model):
    class Meta:
        verbose_name = "tipo de lesion".upper()
        verbose_name_plural = "tipo de lesiones".upper()
    ###############################################
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    
    def __str__(self) -> str:
        return format(self.nombre)

class evento_persona(models.Model):
    class Meta:
        verbose_name = "evento durante el enceuntro".upper()
        verbose_name_plural = "eventos durante los enceuntros".upper()
    ###############################################
    id=models.AutoField(primary_key=True)
    encuentro=models.ForeignKey(encuentro,blank=False,null=False,on_delete=models.CASCADE)
    evento=models.ForeignKey(evento,null=False,blank=False,on_delete=models.CASCADE)
    persona=models.ForeignKey('modulo_contrato.contrato',null=False,blank=False,on_delete=models.CASCADE)
    tipo_lesion=models.ForeignKey(tipo_lesion,null=True,blank=True,on_delete=models.CASCADE)

