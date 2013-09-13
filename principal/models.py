#encoding:utf-8
from django.db import models

class Grados(models.Model):
    idGrado = models.IntegerField(primary_key=True)
    valorGrado = models.IntegerField(max_length=30)
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField()
    fechaCreacion = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % (self.nombre)

class Grupos(models.Model):
    idGrupo = models.IntegerField(max_length=10, primary_key=True)
    codigo = models.CharField(max_length=100)
    idGrado = models.ForeignKey(Grados)
    #fk_Grupos_Grados1 = models.ForeignKey()
    
    def __unicode__(self):
        return "%s" % (self.codigo)
