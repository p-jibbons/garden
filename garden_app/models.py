from django.db import models
from django.urls import reverse


class Plant(models.Model):
    WATER_NEEDS = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    LIGHT_NEEDS = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    TEMPERATURE_NEEDS = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    plant_species = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images/',blank=True,)
    plant_nickname = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True,)
    planted_date = models.DateField(blank=True,)
    retailer_name = models.CharField(max_length=100, blank=True, default='')
    water_needs = models.CharField(max_length=2, blank=True,choices=WATER_NEEDS)
    light_needs = models.CharField(max_length=2, blank=True,choices=LIGHT_NEEDS)
    temperature_needs = models.CharField(max_length=2, blank=True,choices=TEMPERATURE_NEEDS)
    class Meta:
        db_table = 'plant_meta_data'
        ordering = ['planted_date']
        verbose_name = "Plant"
        verbose_name_plural = "Plants"
        get_latest_by = "planted_date"



    def __str__(self):
        return '%s %s'  % ( self.plant_nickname, self.plant_species)

    def get_absolute_url(self):
        return reverse('plant_detail',args=[str(self.id)])



class PlantMeasurement(models.Model):
    ENVIRONMENTAL_DIMENSION = (
        ('light', 'light'),
        ('soil_moisture', 'soil_moisture'),
        ('air_temperature', 'air_temperature'),
    )

    plant_id = models.ForeignKey('Plant', on_delete=models.CASCADE)
    measurement_timestamp = models.DateTimeField()
    environmental_dimension= models.CharField(max_length=100,choices=ENVIRONMENTAL_DIMENSION)
    environmental_value = models.IntegerField()
    class Meta:
        db_table = 'plant_measurements'
        ordering = ['measurement_timestamp']
        verbose_name = "Plant measurment"
        verbose_name_plural = "Plant measurments"
        get_latest_by = "measurement_timestamp'"


    def __str__(self):
        return '%s %s %s'  % (self.plant_id, self.measurement_timestamp, self.environmental_dimension)