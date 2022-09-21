from django.test import TestCase
from .models import Sensor, Report
from django.utils import timezone
from django.db.utils import IntegrityError


class SensorModelTests(TestCase):
    def test_can_create_with_defaults(self):
        sensor = Sensor()
        sensor.save()
        self.assertIs(len(Sensor.objects.all()), 1)

    def test_can_create_with_correct_values(self):
        sensor = Sensor(address='Test address', lat=1.00001, lon=359.999999,
                        iccid='89701010054938823764', stock_number='TEST-0001')
        sensor.save()
        self.assertIs(len(Sensor.objects.all()), 1)

    def test_can_create_with_uuid(self):
        test_id = '335a11da-2c7d-45f4-bb87-908e3ce3bfb1'
        sensor = Sensor(id=test_id)
        sensor.save()
        self.assertIs(len(Sensor.objects.all()), 1)
        self.assertIs(str(Sensor.objects.all()[0].id) == test_id, True)


class ReportModelTests(TestCase):
    def test_can_not_create_empty(self):
        report = Report()
        try:
            report.save()
        except IntegrityError as e:
            self.assertRaisesMessage(
                e,
                'null value in column "sensor_id" of relation "sensors_report" violates not-null constraint'
            )

    def test_can_create_only_with_sensor(self):
        sensor = Sensor()
        sensor.save()
        report = Report(sensor=sensor)
        report.save()
        self.assertIs(len(Report.objects.all()), 1)

    def test_can_create_with_correct_values(self):
        sensor = Sensor()
        sensor.save()
        report = Report(sensor=sensor, datetime=timezone.now(),
                        container_fill_state=100, container_temperature=10,
                        sensor_temperature=10, container_humidity=10,
                        sensor_humidity=10, sensor_position=None,
                        sensor_x=100, sensor_y=100, sensor_z=100,
                        sensor_longitude=359.999999, sensor_latitude=0.000001,
                        sensor_error='', sensor_lcv=10, sensor_hcv=10,
                        sensor_soc=10, sensor_height=10, electronic_seal_state='',
                        command_status_json='')
        report.save()
        self.assertIs(len(Report.objects.all()), 1)


class SensorViewSetTests(TestCase):
    pass


class ReportViewSetTests(TestCase):
    pass
