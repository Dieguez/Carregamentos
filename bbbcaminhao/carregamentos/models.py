from django.db import models, transaction
import datetime
from django.utils.encoding import python_2_unicode_compatible
import webcam.admin
from webcam.fields import CameraField
import pytz
from django.utils import timezone
from django.utils import formats
import os
from django.core.exceptions import ValidationError
from django.core.files import File

from django_boto.s3.storage import S3Storage
from django.conf import settings



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
    foto = CameraField('foto', format='jpeg', null=True, blank=True, upload_to='media/caminhao')
    volume = models.DecimalField(max_digits=20, decimal_places=2, null=True)

    # ...
    def __str__(self):
        return self.placa+"-"+self.motorista

    def admin_image(self):
        # return '<img src="../../../media/%s" width=80 height=80 />' % self.foto
        return '<img src="https://s3-sa-east-1.amazonaws.com/bbbcaminhao/%s" width=80 height=80 />' % self.foto
        
    admin_image.allow_tags = True

    def save(self):
        if not self.data_criacao:
            self.data_criacao = datetime.datetime.today()
        self.data_alteracao = datetime.datetime.today()
        self.volume = self.largura*self.profundidade*self.altura
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
    photo = CameraField('foto', format='jpeg', null=True, blank=True, upload_to='media')
    foto = models.FileField(upload_to='media', blank=True, null=True)
    data_criacao = models.DateTimeField(editable=False)
    data_alteracao = models.DateTimeField(editable=False)
    #is_active = models.BooleanField()
    id_caminhao = models.CharField(max_length=100)
    caminhao = models.ForeignKey(Caminhao)
    manifesto = models.CharField(max_length=100, unique=True, null=True)
    tiquete = models.CharField(max_length=100, unique=True, null=True)
    
    def __str__(self):
        return self.caminhao.motorista 

    def admin_image(self):
        # return '<img src="../../../media/%s" width=80 height=80 />' % self.photo
        return '<img src="https://s3-sa-east-1.amazonaws.com/bbbcaminhao/%s" width=80 height=80 />' % self.photo
        # https://s3-sa-east-1.amazonaws.com/bbbcaminhao/media/cad67751-84fd-4ad7-bf4b-26296b8d67e9.jpeg

    admin_image.allow_tags = True

    def clean(self):
        try:
            self.caminhao = Caminhao.objects.get(pk=self.id_caminhao)
        except Exception, e:
            raise ValidationError('Caminhao Invalido!')   


    def save(self):

        if not self.id:
            self.data_criacao = datetime.datetime.today()
            self.data = datetime.datetime.today()
        self.data_alteracao = datetime.datetime.today()

        # f = open(self.photo.path, 'w')
        # self.foto = File(f)         

        # import pdb; pdb.set_trace()

        self.foto = self.photo

        if not self.id:
            try:
                last_carregamento = Carregamento.objects.filter(caminhao=self.caminhao).order_by('-id')[0]
                duration = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)-last_carregamento.data
                if last_carregamento:
                    Carregamento.objects.filter(id=last_carregamento.id).update(tiquete=self.tiquete)
            except Exception, e:
                duration=0
                
            self.tiquete = None 

            if duration and duration.days==0:
                self.duracao = duration  

          
        super(Carregamento, self).save()  


            
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Carregamento, dispatch_uid="update_stock_count")
def upload_to_s3(sender, instance, **kwargs):
   
    import boto
    from boto.s3.key import Key
    # set boto lib debug to critical
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    # connect to the bucket
    conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID,
                    settings.AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(bucket_name)
    # go through each version of the file
    # key = '%s.png' % id
    # fn = '/var/www/data/%s.png' % id
    # create a key to keep track of our file in the storage 
    k = Key(bucket)
    k.key = instance.photo.name
    k.set_contents_from_filename(instance.photo.path)
    # we need to make it public so it can be accessed publicly
    # using a URL like http://s3.amazonaws.com/bucket_name/key
    k.make_public()
    # remove the file from the web server
    # os.remove(fn)
    
@receiver(post_save, sender=Caminhao, dispatch_uid="caminhao")
def upload_to_s3_caminhao(sender, instance, **kwargs):
   
    import boto
    from boto.s3.key import Key
    # set boto lib debug to critical
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    # connect to the bucket
    conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID,
                    settings.AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(bucket_name)
    # go through each version of the file
    # key = '%s.png' % id
    # fn = '/var/www/data/%s.png' % id
    # create a key to keep track of our file in the storage 
    k = Key(bucket)
    k.key = instance.foto.name
    k.set_contents_from_filename(instance.foto.path)
    # we need to make it public so it can be accessed publicly
    # using a URL like http://s3.amazonaws.com/bucket_name/key
    k.make_public()
    # remove the file from the web server
    # os.remove(fn)


     

        
    






