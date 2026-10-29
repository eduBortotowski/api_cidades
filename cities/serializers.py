from rest_framework import serializers

from cities.models import City


class CitySerializer(serializers.ModelSerializer):
    """Serialize city records for the REST API."""

    class Meta:
        model = City
        fields = ["id", "name"]
