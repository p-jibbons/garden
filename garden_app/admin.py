from django.contrib import admin

from .models import Plant,PlantMeasurement


class Plantadmin(admin.ModelAdmin):
    fields = [ 'plant_species', 'image', 'plant_nickname', 'description', 'planted_date',
              'retailer_name', 'water_needs', 'light_needs', 'temperature_needs']
admin.site.register(Plant, Plantadmin)

class PlantMeasurementadmin(admin.ModelAdmin):
    fields = ['plant_id', 'measurement_timestamp', 'environmental_dimension', 'environmental_value']
admin.site.register(PlantMeasurement, PlantMeasurementadmin)


