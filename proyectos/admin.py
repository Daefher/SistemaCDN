from django.contrib import admin
from .models import proyecto
from .models import clientes
from .models import progreso
# Register your models here.
admin.site.register(proyecto)
admin.site.register(clientes)
admin.site.register(progreso)
