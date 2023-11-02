from django.db import models

# Create your models here.
class tipo_persona(models.Model):
    class Meta:
        verbose_name = "Tipo de Persona".upper()
        verbose_name_plural = "Tipo de Personas".upper()
    #############################################
    
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(blank=False,null=False,max_length=30)
    estado=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return format(self.descripcion.upper())
class persona(models.Model):
    class Meta:
        verbose_name = "Persona".upper()
        verbose_name_plural = "Personas".upper()
    
    id=models.AutoField(primary_key=True)
    tipo_persona=models.ForeignKey(tipo_persona,blank=False,null=False,on_delete=models.CASCADE)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    alias=models.CharField(max_length=30)
    sexos_list=[
        ('M','MASCULINO'),
        ('F','FEMENINO'),
        ]
    sexo=models.CharField(choices=sexos_list,max_length=1,default='M')
    fecha_nacimiento=models.DateField()
    estatura=models.FloatField(default=0)
    peso=models.FloatField(default=0)
    foto=models.ImageField(blank=True,null=True,upload_to='jugador/',default='jugador/jugador_default.png')
    estado=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        txt=("{0} {1}")
        return txt.format(self.nombres,self.apellidos)

class contrato(models.Model):
    class Meta:
        verbose_name = "Contrato".upper()
        verbose_name_plural = "Contratos".upper()
    ##################################################
    id=models.AutoField(primary_key=True)
    persona=models.ForeignKey(persona, blank=False,null=False, on_delete=models.CASCADE)
    tipo_contrato_lis=[
        ('P','Préstamo'.upper()),
        ('C','compra'.upper()),
        ('L','libre'.upper()),
        ('R','Renovación'.upper()),
        ('S','selección'.upper()),
    ]
    tipo_contrato=models.CharField(max_length=1,choices=tipo_contrato_lis)
    nuevo_club=models.ForeignKey('modulo_equipo.equipo',blank=True,null=True,on_delete=models.CASCADE, related_name='nuevo_club')
    ultimo_club=models.ForeignKey('modulo_equipo.equipo',blank=True,null=True,on_delete=models.CASCADE, related_name='ultimo_club')
    valor=models.FloatField(default=0, null=True,blank=True)
    fecha_inicio=models.DateField(null=True,blank=True)
    fecha_fin=models.DateField(null=True,blank=True)
    dorsal=models.PositiveSmallIntegerField(blank=False,null=False)
    posicion_list=[
        ('Portero','Portero'),
        ('Defensa: Defensa central, lateral, libre y carrilero','Defensa: Defensa central, lateral, libre y carrilero'),
        ('Centrocampista: Pivote, media punta, volante e interior','Centrocampista: Pivote, media punta, volante e interior'),
        ('Delantero: Segundo delantero, delantero centro y extremo','Delantero: Segundo delantero, delantero centro y extremo'),
    ]
    posicion=models.CharField(choices=posicion_list,max_length=100)
    estado=models.BooleanField(default=True)
    def __str__(self):
        if self.tipo_contrato=='P':
            txt=("{0} - {1} Prestamo")
        elif self.tipo_contrato=='C':
            txt=("{0} - {1} Compra")
        elif self.tipo_contrato=='L':
            txt=("{0} - {1} libre")
        elif self.tipo_contrato=='S':
            txt=("{0} - {1} Selección")
        elif self.tipo_contrato=='R':
            txt=("{0} - {1} Renovación")
            
        return txt.format(self.persona,self.nuevo_club)
    