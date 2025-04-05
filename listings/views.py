from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_queryset(self):
        queryset = Property.objects.all()
        ptype = self.request.query_params.get('type')
        if ptype:
            queryset = queryset.filter(type=ptype)
        return queryset
