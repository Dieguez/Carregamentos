from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
import webcam.admin
from webcam.fields import CameraField
import pytz
from django.utils import timezone
from django.utils import formats



# Create your models here.


class Caminhao(models.Model):
    placa = models.CharField(max_length=7)
    largura = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    profundidade = models.DecimalField(max_digits=5, decimal_places=2)
    motorista = models.CharField(max_length=500)
    data_criacao = models.DateTimeField(editable=False)
    data_alteracao = models.DateTimeField(editable=False)
    #is_active = models.BooleanField(editable=False, default=True)
    codigo_barras = models.CharField(max_length=50, primary_key=True)
    
    # ...
    def __str__(self):
        return self.placa+"-"+self.motorista

    def save(self):
        if not self.data_criacao:
            self.data_criacao = datetime.datetime.today()
        self.data_alteracao = datetime.datetime.today()
        super(Caminhao, self).save()

    class Meta(object):
        verbose_name = 'Caminhao'
        verbose_name_plural = 'Caminhoes'


class Frente(models.Model):
    nome = models.CharField(max_length=2000)
    data_criacao = models.DateTimeField(editable=False)
    data_alteracao = models.DateTimeField(editable=False)
    #is_active = models.BooleanField()
    # ...
    def __str__(self):
        return self.nome 

    def save(self):
        if not self.id:
            self.data_criacao = datetime.datetime.today()
        self.data_alteracao = datetime.datetime.today()
        super(Frente, self).save()   


class Carregamento(models.Model):
    frente = models.ForeignKey(Frente, blank=True, null=True)
    data = models.DateTimeField(editable=False) 
    duracao = models.DurationField(editable=False, default=datetime.timedelta())
    #path_foto = models.CharField(max_length=2000)
    #picture = CameraField(null=True)
    photo = CameraField('foto', format='jpeg', null=True, blank=True, upload_to='carregamentos-photo')
    foto = models.FileField(upload_to='carregamentos-photo', blank=True, null=True)
    data_criacao = models.DateTimeField(editable=False)
    data_alteracao = models.DateTimeField(editable=False)
    #is_active = models.BooleanField()
    id_caminhao = models.CharField(max_length=100)
    caminhao = models.ForeignKey(Caminhao, blank=True, null=True)
    
    def __str__(self):
        return self.caminhao.motorista 

    def save(self):
        if not self.id:
            self.data_criacao = datetime.datetime.today()
            self.data = datetime.datetime.today()
        self.data_alteracao = datetime.datetime.today()

        
        self.caminhao = Caminhao.objects.get(pk=self.id_caminhao)

        # import pdb; pdb.set_trace()

        self.foto = self.photo

        try:
            last_carregamento = Carregamento.objects.filter(caminhao=self.caminhao).order_by('-id')[0]
            duration = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)-last_carregamento.data
        except Exception, e:
            duration=0
            

        if duration and duration.days==0:
            self.duracao = duration  

        super(Carregamento, self).save()  


     

        
    






