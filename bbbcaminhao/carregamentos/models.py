from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Caminhao(models.Model):
    placa = models.CharField(max_length=7)
    largura = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    profundidade = models.DecimalField(max_digits=5, decimal_places=2)
    motorista = models.CharField(max_length=500)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    is_active = models.BooleanField()
    # ...
    def __str__(self):
        return self.placa+"-"+self.motorista

    def save(self):
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        super(Caminhao, self).save()

    class Meta(object):
        verbose_name = 'Caminhao'
        verbose_name_plural = 'Caminhoes'

@python_2_unicode_compatible
class Frente(models.Model):
    nome = models.CharField(max_length=2000)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    is_active = models.BooleanField()
    # ...
    def __str__(self):
        return self.nome 

    def save(self):
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        super(Frente, self).save()   

@python_2_unicode_compatible
class Carregamento(models.Model):
    caminhao = models.ForeignKey(Caminhao)
    frente = models.ForeignKey(Frente)
    data = models.DateTimeField(editable=False) 
    duracao = models.DurationField()
    path_foto = models.CharField(max_length=2000)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.caminhao.motorista 

    def save(self):
        if not self.id:
            self.created_at = datetime.datetime.today()
            self.data = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        super(Carregamento, self).save()  
    






