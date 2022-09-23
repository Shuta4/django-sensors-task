from django.urls import include, path
from rest_framework_extensions.routers import ExtendedSimpleRouter

from . import views

router = ExtendedSimpleRouter()
router.register(r'sensors', views.SensorViewSet, basename='sensor')\
    .register(r'reports', views.ReportViewSet, basename='sensors-report',
              parents_query_lookups=['sensor'])
router.register(r'reports', views.ReportViewSet, basename='report')

urlpatterns = [
    path(r'', include(router.urls))
]
