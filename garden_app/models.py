from django.db import models
from django.urls import reverse

ENVIRONMENTAL_DIMENSION = (
        ('light', 'light'),
        ('soil_moisture', 'soil_moisture'),
        ('air_temperature', 'air_temperature'),
    )

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

class PlantMeasurement(models.Model):


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





class Plant(models.Model):
    plant_species = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images/',blank=True,)
    plant_nickname = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True,)
    planted_date = models.DateField(blank=True,)
    retailer_name = models.CharField(max_length=100, blank=True, default='')
    water_needs = models.CharField(max_length=2, blank=True,choices=WATER_NEEDS)
    light_needs = models.CharField(max_length=2, blank=True,choices=LIGHT_NEEDS)
    temperature_needs = models.CharField(max_length=2, blank=True,choices=TEMPERATURE_NEEDS)

    arduino_id = models.ForeignKey('ArduinoBoard', on_delete=models.CASCADE,null=True,blank=True,related_name="plants")
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







class ArduinoBoard(models.Model):

    ARDUINO_MODEL_CHOICES = models.TextChoices('ARDUINO_MODEL_CHOICES', 'UNO MEGA')


    serial_number = models.CharField(max_length=100,primary_key=True,unique=True)
    model_name = models.CharField(max_length=100,choices=ARDUINO_MODEL_CHOICES.choices)


    def __str__(self):
        return '%s - %s'  % (self.model_name, self.serial_number)




class ArduinoPin(models.Model):
    ARDUINO_PIN_CHOICES = models.TextChoices('ARDUINO_PIN_CHOICES', 'a:0:i a:1:i a:2:i a:3:i a:4:i a:5:i a:6:i a:7:i a:8:i a:9:i a:10:i a:11:i a:12:i a:13:i a:14:i a:15:i')
    arduino_id = models.ForeignKey('ArduinoBoard', on_delete=models.CASCADE, null=True, blank=True)
    plant_id = models.ForeignKey('Plant', on_delete=models.CASCADE, null=True, blank=True)
    pin_number = models.CharField(max_length=10,choices=ARDUINO_PIN_CHOICES.choices)
    environmental_dimension = models.CharField(max_length=100, choices=ENVIRONMENTAL_DIMENSION)
    sensor_low = models.IntegerField(null=True, blank=True)
    sensor_high = models.IntegerField(null=True, blank=True)
    is_collecting = models.BooleanField(default=False)


    class Meta:
        unique_together = [['arduino_id', 'pin_number']]
    def __str__(self):
        return '%s  %s %s'   % (self.arduino_id, self.pin_number, self.environmental_dimension)