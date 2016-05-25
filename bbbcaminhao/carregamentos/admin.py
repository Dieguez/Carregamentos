from django.contrib import admin
from daterange_filter.filter import DateRangeFilter
from .models import Caminhao, Carregamento, Frente
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from webcam import widgets
from webcam.fields import CameraField

FORMFIELD_FOR_DBFIELD_DEFAULTS[CameraField] = {'widget': widgets.CameraWidget}

from django import forms
import time


class CaminhaoForm(forms.ModelForm):
    codigo_barras = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Caminhao
        fields = ["placa", "largura", "altura", "profundidade", "motorista", "codigo_barras"]
        widgets = {
            'codigo_barras': forms.PasswordInput(),
        }

class CarregamentoForm(forms.ModelForm):
    id_caminhao = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Carregamento
        fields = ['frente', 'photo', 'id_caminhao']
        widgets = {
            'id_caminhao': forms.PasswordInput(),
        }


class CarregamentoResource(resources.ModelResource):

    class Meta:
        model = Carregamento
        fields = ("caminhao__placa", "caminhao__motorista", "data", "duracao", "frente__nome", )
        # widgets = {
        #         'data': {'format': '%d:%m:%Y %h:%M'},
        #         'duracao': {'format': '%h:%M'},
        #         }
    

class CarregamentoAdmin(ImportExportModelAdmin):
	list_display = ["caminhao", "frente", "data", "data_alteracao", "duracao", "admin_image"]

	# def duracao_viagem(self, obj):
	# 	total_seconds = int(obj.duracao.total_seconds())
	# 	hours = total_seconds // 3600
	# 	minutes = (total_seconds % 3600) // 60

	# 	return '{} horas {} min'.format(hours, minutes)

	class Meta:
		model = Carregamento
		fields = ("caminhao__placa", "caminhao__motorista", "data", "duracao")

	search_fields = ["caminhao__placa", "frente__nome", "data", "data_alteracao"]
	list_filter = ["caminhao__placa", "frente__nome", ("data", DateRangeFilter)]
	#raw_id_fields = ["caminhao"]
	resource_class = CarregamentoResource
	form = CarregamentoForm


class CaminhaoAdmin(admin.ModelAdmin):
	list_display = ["placa", "largura", "altura", "profundidade", "motorista", "data_criacao", "data_alteracao"]
	search_fields = ["placa", "largura", "altura", "profundidade", "motorista", "data_criacao", "data_alteracao"]
	list_filter = ["placa", "largura", "altura", "profundidade", "motorista", "data_criacao", "data_alteracao"]
	form = CaminhaoForm

class FrenteAdmin(admin.ModelAdmin):
	list_display = ["nome", "data_criacao", "data_alteracao"]	
	search_fields = ["nome", "data_criacao", "data_alteracao"]	
	list_filter = ["nome", "data_criacao", "data_alteracao"]





admin.site.register(Caminhao, CaminhaoAdmin)
admin.site.register(Carregamento, CarregamentoAdmin)
admin.site.register(Frente, FrenteAdmin)









