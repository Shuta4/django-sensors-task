from rest_framework import serializers
from .models import Sensor, Report


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('url', 'id', 'address', 'lat', 'lon', 'iccid', 'stock_number')


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('url', 'id', 'sensor', 'datetime',
                  'container_fill_state', 'container_temperature',
                  'sensor_temperature', 'container_humidity', 'sensor_humidity',
                  'sensor_position', 'sensor_x', 'sensor_y', 'sensor_z',
                  'sensor_longitude', 'sensor_latitude', 'sensor_error',
                  'sensor_lcv', 'sensor_hcv', 'sensor_soc', 'sensor_height',
                  'electronic_seal_state', 'command_status_json')