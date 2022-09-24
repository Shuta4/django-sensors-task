from django.db import models
import uuid
from django.utils import timezone


class Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    address = models.TextField(blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    iccid = models.CharField(max_length=30, blank=True)
    stock_number = models.CharField(max_length=30, blank=True)


class Report(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, blank=False, null=False)
    datetime = models.DateTimeField(default=timezone.now, blank=False, null=False)
    container_fill_state = models.IntegerField(null=True)
    container_temperature = models.IntegerField(null=True)
    sensor_temperature = models.IntegerField(null=True)
    container_humidity = models.IntegerField(null=True)
    sensor_humidity = models.IntegerField(null=True)
    sensor_position = models.IntegerField(null=True)
    sensor_x = models.IntegerField(null=True)
    sensor_y = models.IntegerField(null=True)
    sensor_z = models.IntegerField(null=True)
    sensor_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    sensor_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    sensor_error = models.TextField(blank=True)
    sensor_lcv = models.IntegerField(null=True)
    sensor_hcv = models.IntegerField(null=True)
    sensor_soc = models.IntegerField(null=True)
    sensor_height = models.IntegerField(null=True)
    electronic_seal_state = models.CharField(max_length=30, blank=True)
    command_status_json = models.TextField(blank=True)
