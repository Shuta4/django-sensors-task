from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'sensors', views.SensorViewSet, basename='sensor')
router.register(r'reports', views.ReportViewSet, basename='report')

urlpatterns = [
    path(r'', include(router.urls))
]
