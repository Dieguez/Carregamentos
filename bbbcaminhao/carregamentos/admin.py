from django.contrib import admin
from daterange_filter.filter import DateRangeFilter
from .models import Caminhao, Carregamento, Frente
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from webcam import widgets
from webcam.fields import CameraField

FORMFIELD_FOR_DBFIELD_DEFAULTS[CameraField] = {'widget': widgets.CameraWidget}


class CarregamentoAdmin(ImportExportModelAdmin):
	list_display = ["caminhao", "frente", "data", "duracao"]
	search_fields = ["caminhao__placa", "frente__nome", "data"]
	list_filter = ["caminhao__placa", "frente__nome", ("data", DateRangeFilter)]



class CaminhaoAdmin(admin.ModelAdmin):
	list_display = ["placa", "largura", "altura", "profundidade", "motorista", "created_at", "updated_at"]
	search_fields = ["placa", "largura", "altura", "profundidade", "motorista", "created_at", "updated_at"]
	list_filter = ["placa", "largura", "altura", "profundidade", "motorista", "created_at", "updated_at"]

class FrenteAdmin(admin.ModelAdmin):
	list_display = ["nome", "created_at", "updated_at"]	
	search_fields = ["nome", "created_at", "updated_at"]	
	list_filter = ["nome", "created_at", "updated_at"]	



admin.site.register(Caminhao, CaminhaoAdmin)
admin.site.register(Carregamento, CarregamentoAdmin)
admin.site.register(Frente, FrenteAdmin)









