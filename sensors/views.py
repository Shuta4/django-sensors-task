from rest_framework import viewsets
from rest_framework_extensions import mixins
from .models import Sensor, Report
from .serializers import SensorSerializer, ReportSerializer


class SensorViewSet(viewsets.ModelViewSet, mixins.NestedViewSetMixin):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
