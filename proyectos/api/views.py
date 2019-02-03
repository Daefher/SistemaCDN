#generic
from django.db.models import Q
from rest_framework import generics, mixins
from proyectos.models import proyecto
from .permissions import IsOwnerOrReadOnly
from .serializers import proyectoPostSerializer

class ProyectoPostAPIView(mixins.CreateModelMixin,generics.ListAPIView): #Detail View
    lookup_field        = 'folio'
    serializer_class    = proyectoPostSerializer
    # permission_classes  = [IsOwnerOrReadOnly]
    # queryset        = proyecto.objects.all()    #
    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = proyecto.objects.all()
        else:
            qs = proyecto.objects.filter(
            autor = self.request.user)
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter((
            Q(enajenante = query) |
            Q(adquirente = query)) &
            Q(autor = self.request.user)
            ).distinct()
        return qs
    def perform_create(self, serializer):
        serializer.save(autor = self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs )


class ProyectoRudView(generics.RetrieveUpdateDestroyAPIView): #Detail View
    lookup_field        = 'folio'
    serializer_class    = proyectoPostSerializer
    permission_classes  = [IsOwnerOrReadOnly]
    # queryset        = proyecto.objects.all()

    def get_queryset(self):
        return proyecto.objects.all()
