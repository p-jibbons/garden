from django.contrib import admin

from .models import Plant,PlantMeasurement,ArduinoBoard, ArduinoPin

class ArduinoPinInline(admin.TabularInline):
    model = ArduinoPin

class Plantadmin(admin.ModelAdmin):
    fields = [ 'plant_species', 'image', 'plant_nickname', 'description', 'planted_date',
              'retailer_name', 'water_needs', 'light_needs', 'temperature_needs','arduino_id']


class PlantMeasurementadmin(admin.ModelAdmin):
    fields = ['plant_id', 'measurement_timestamp', 'environmental_dimension', 'environmental_value']
    list_display = ['plant_id', 'measurement_timestamp', 'environmental_dimension', 'environmental_value']





class ArduinoPinadmin(admin.ModelAdmin):
    list_display = [ 'arduino_id','plant_id', 'environmental_dimension', 'pin_number','is_collecting']
    fields = [ 'arduino_id','plant_id', 'environmental_dimension', 'pin_number','is_collecting']

    list_filter = [ 'arduino_id','plant_id', 'environmental_dimension', 'pin_number','is_collecting']
    list_editable =[ 'plant_id', 'environmental_dimension', 'pin_number','is_collecting']


class ArduinoBoardadmin(admin.ModelAdmin):
    inlines = [ArduinoPinInline,]
    fields = [ 'serial_number', 'model_name']
    list_display = [ 'serial_number', 'model_name']

    # list_filter = ['arduino_id', 'environmental_dimension']
    # list_editable =[  'environmental_dimension', 'pin_number','is_collecting']





admin.site.register(Plant, Plantadmin)
admin.site.register(PlantMeasurement, PlantMeasurementadmin)
admin.site.register(ArduinoBoard,ArduinoBoardadmin)
admin.site.register(ArduinoPin,ArduinoPinadmin)


