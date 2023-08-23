from unittest.mock import patch, Mock

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from characters.models import Character
from characters.serializers import CharacterSerializer

RANDOM_CHARACTER_URL = reverse("characters:random-character")


class Test(APITestCase):
    def test_returns_random_character(self):
        # Arrange
        # Create and save Character objects
        character1 = Character.objects.create(
            api_id=1,
            name="Character 1",
            status=Character.StatusChoices.ALIVE,
            species="Species 1",
            gender=Character.GenderChoices.MALE,
            image="https://image1.com",
        )
        character2 = Character.objects.create(
            api_id=2,
            name="Character 2",
            status=Character.StatusChoices.DEAD,
            species="Species 2",
            gender=Character.GenderChoices.FEMALE,
            image="https://image2.com",
        )
        character3 = Character.objects.create(
            api_id=3,
            name="Character 3",
            status=Character.StatusChoices.UNKNOWN,
            species="Species 3",
            gender=Character.GenderChoices.GENDERLESS,
            image="https://image3.com",
        )

        # Act
        response = self.client.get(
            RANDOM_CHARACTER_URL
        )  # Assuming the endpoint is "/random-character/"

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", response.data)
        self.assertIn("api_id", response.data)
        self.assertIn("name", response.data)
        self.assertIn("status", response.data)
        self.assertIn("species", response.data)
        self.assertIn("gender", response.data)
        self.assertIn("image", response.data)
