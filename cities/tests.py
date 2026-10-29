from rest_framework import status
from rest_framework.test import APITestCase

from cities.models import City


class CityListAPITestCase(APITestCase):
    """Tests for GET /api/cities/."""

    url = "/api/cities/"

    def test_list_empty_returns_200(self) -> None:
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

    def test_list_with_items_returns_200(self) -> None:
        City.objects.create(name="Recife")
        City.objects.create(name="Olinda")

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        payload = response.json()
        self.assertEqual(len(payload), 2)
        self.assertEqual([item["name"] for item in payload], ["Olinda", "Recife"])
