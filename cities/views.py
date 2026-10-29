from rest_framework import viewsets

from cities.models import City
from cities.serializers import CitySerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only list and detail for cities."""

    queryset = City.objects.all()
    serializer_class = CitySerializer
