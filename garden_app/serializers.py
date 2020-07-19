from rest_framework import serializers
from garden_app.models import  Plant, PlantMeasurement ,ArduinoPin

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


class PlantMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantMeasurement
        fields = ['plant_id', 'measurement_timestamp', 'environmental_dimension', 'environmental_value']

class ArduinoPinSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArduinoPin
        fields = [ 'arduino_id','plant_id', 'environmental_dimension', 'pin_number','is_collecting']








