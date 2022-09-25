import argparse
import datetime
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
import random
from ...models import Sensor, Report


class Command(BaseCommand):
    help = 'Creates random reports for all sensors for each day'

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument(
            '-f', '--from',
            help='Start reports creation from this day in iso format',
            type=datetime.date.fromisoformat,
            default=datetime.date.today()
        )
        parser.add_argument(
            '-t', '--to',
            help='End reports creation on this day in iso format',
            type=datetime.date.fromisoformat,
            default=datetime.date.today()
        )

    def handle(self, *args, **options):
        if options['from'] > options['to']:
            raise ValueError('Period can not start with date greater then end date')

        sensors = Sensor.objects.all()
        date = options['from']
        with transaction.atomic():
            while date <= options['to']:
                for sensor in sensors:
                    report = Report(sensor=sensor)

                    report.datetime = timezone.now().replace(
                        year=date.year, month=date.month, day=date.day)

                    report.container_fill_state = random.randint(0, 100)
                    report.container_temperature = random.randint(-10, 100)
                    report.sensor_temperature = random.randint(-10, 100)
                    report.container_humidity = random.randint(0, 100)
                    report.sensor_humidity = random.randint(0, 100)
                    report.sensor_position = random.randint(0, 1)
                    report.sensor_x = random.randint(0, 360000)
                    report.sensor_y = random.randint(0, 360000)
                    report.sensor_z = random.randint(0, 360000)
                    report.sensor_longitude = round(random.random() * 1000 % 360, 6)
                    report.sensor_latitude = round(random.random() * 1000 % 360, 6)
                    report.sensor_lcv = random.randint(0, 100)
                    report.sensor_hcv = random.randint(0, 100)
                    report.sensor_soc = random.randint(0, 100)
                    report.sensor_height = random.randint(0, 10000)

                    report.save()

                date += datetime.timedelta(days=1)
