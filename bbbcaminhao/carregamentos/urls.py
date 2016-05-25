from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),   
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
 {'document_root': settings.STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



