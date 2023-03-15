from django.db import models


class Sensor(models.Model):
    #id
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True, default='')


class Measurement(models.Model):
    #id
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    measurement_date = models.DateTimeField(auto_now=True)
    photo_url = models.ImageField(upload_to='photos', blank=True)
