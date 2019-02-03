from .views import ProyectoRudView,ProyectoPostAPIView
from django.urls import re_path

app_name = 'proyectos'

urlpatterns = [
    re_path(r'^$', ProyectoPostAPIView.as_view(), name='proyecto-create'),
    re_path(r'^(?P<folio>\d+)/$', ProyectoRudView.as_view(), name='proyecto-rud'),

]
