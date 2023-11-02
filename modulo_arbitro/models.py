from django.db import models

# Create your models here.
class arbitro(models.Model):
    class Meta:
        verbose_name = "arbitro".upper()
        verbose_name_plural = "arbitros".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=120)
    fecha_nacimiento=models.DateField()
    list_choices_tipo_arbitro=[
        ("P","Principal".upper()),
        ("J","Juez de Linea".upper()),
        ("C","cuarto hombre".upper()),
        ("V","VAR (Árbitro asistente de video)".upper())
        ]
    tipo_arbitro=models.CharField(choices=list_choices_tipo_arbitro,max_length=1)
    pais=models.ForeignKey('modulo_competicion.pais',blank=False,null=False,on_delete=models.CASCADE)
    estado=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        txt=("{0} {1} ({2})")
        return txt.format(self.nombres,self.apellidos, self.pais)
    
class terna_arbitral(models.Model):
    class Meta:
        verbose_name = "Terna Arbitral".upper()
        verbose_name_plural = "Ternas Arbitrales".upper()
    ############################################# 
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    estado=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return format(self.nombre)

class tipo_terna(models.Model):
    class Meta:
        verbose_name = "tipo de Terna Arbitral".upper()
        verbose_name_plural = "Tipo de Ternas Arbitrales".upper()
    ############################################# 
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=50)
    sigla=models.CharField(max_length=3)
    
    def __str__(self) -> str:
        txt=("{0} ({1})")
        return txt.format(self.descripcion,self.sigla)

class detalle_terna(models.Model):
    class Meta:
        verbose_name = "Detalle de Terna Arbitral".upper()
        verbose_name_plural = "Detalle de Ternas Arbitrales".upper()
    #############################################
    id=models.AutoField(primary_key=True)
    terna_arbitral=models.ForeignKey(terna_arbitral,null=False,blank=False,on_delete=models.CASCADE)
    arbitro=models.ForeignKey(arbitro,null=False,blank=False,on_delete=models.CASCADE)
    tipo_terna=models.ForeignKey(tipo_terna,null=False,blank=False,on_delete=models.CASCADE)
    estado_juego=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        txt=("{0} | {1} | {2}")
        return txt.format(self.terna_arbitral,self.arbitro,self.tipo_terna)
    
    