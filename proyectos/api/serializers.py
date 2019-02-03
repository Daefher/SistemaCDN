from rest_framework import serializers
from proyectos.models import proyecto


class proyectoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model   = proyecto
        fields  = [
                    'folio',
                    'tomo',
                    'slug',
                    'numero_instrumento',
                    'enajenante',
                    'adquirente',
                    'tipo',
                    'fecha',
                    'autor',
                    'localizacion',
                    'prueba',
                ]
        read_only_fields = ['autor',]

        def validate_title(self, value):
            qs = proyecto.objects.filter(numero_instrumento_iexact = value)
            if self.instance:
                qs = qs.exclude(pk = self.instance.pk)
            if qs.exist():
                raise serializers.ValidationError("El numero instrumento ya existe")
            return value

    # Converts to JSON
    # Validations for data passed
