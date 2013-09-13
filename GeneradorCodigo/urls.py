from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','principal.views.inicio'),
    url(r'^grados/$','principal.views.inicio_grados',name='vergrados_view'),
    url(r'^nuevo/grado/$', 'principal.views.nuevoGrado',name='nuevogrado'),
    url(r'^grados/editar/(?P<id_grado>.*)', 'principal.views.editarGrado'),
    url(r'^grados/borrar/(?P<id_grado>.*)', 'principal.views.borrarGrado'),

    url(r'^grupos/$','principal.views.inicio_grupos',name='vergrupos_view'),
    url(r'^nuevo/grupo/$', 'principal.views.nuevoGrupo',name='nuevogrupo'),
    url(r'^grupos/editar/(?P<id_grupo>.*)', 'principal.views.editarGrupo'),
    url(r'^grupos/borrar/(?P<id_grupo>.*)', 'principal.views.borrarGrupo'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)