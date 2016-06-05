from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from . import views

admin.site.site_header = 'Controle de carregamentos'

urlpatterns = [
    url(r'^$', views.index, name='index'),   
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
 {'document_root': settings.STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



