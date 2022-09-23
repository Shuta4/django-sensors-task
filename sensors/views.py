from rest_framework import viewsets
from rest_framework_extensions import mixins
from .models import Sensor, Report
from .serializers import SensorSerializer, ReportSerializer


class SensorViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ReportViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
