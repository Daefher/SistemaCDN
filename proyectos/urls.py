from django.urls import path
from . import views


app_name = 'proyecto'

urlpatterns = [
    path('',views.vista_proyectos,name="general"),
    path('proyectos-actuales/', views.vista_proyectos_actuales,name="actuales"),
    path('agregar-proyecto/', views.vista_agregar_proyecto,name="agregar"),
    path('agregar-progreso/', views.vista_agregar_progreso,name="progreso"),
    path('<slug>',views.vista_detalle_proyecto,name='detalles'),
    path('progress/<id>', views.agregar_progreso,name="agregar_pro"),
    path('progreso-busqueda/', views.busqueda,name="buscar"),
    path('editar/<id>/',views.editar,name="editar"),
]
