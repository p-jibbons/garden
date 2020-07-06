from django.test import TestCase
from django.test import TestCase
from .models import Plant
from django.contrib.auth.models import User


# class PlantModelTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='test_user', email='test_user@…', password='top_secret')
#         Plant.objects.create(plant_species = 'test_species',owner_id =1,planted_date= '2020-10-10')
#
#
#     def test_text_content(self):
#         plant = Plant.objects.get(id=1)
#         expected_object_species = f'{plant.plant_species}'
#         self.assertEqual(expected_object_species, 'test_species')
#
