from rest_framework import serializers
from garden_app.models import  Plant, PlantMeasurement

from django.contrib.auth.models import User




class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username']



class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ['plant_species', 'plant_nickname', 'description', 'planted_date',
                  'retailer_name', 'water_needs', 'light_needs', 'temperature_needs']


class PlantMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlantMeasurement
        fields = ['plant_id', 'measurement_timestamp', 'environmental_dimension', 'environmental_value']


