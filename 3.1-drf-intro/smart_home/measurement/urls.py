from django.urls import path

from measurement.views import CreateListSensor, CreateMeasurement, RetrieveUpdateSensor

urlpatterns = [
     path('sensors/', CreateListSensor.as_view()),
     path('measurements/', CreateMeasurement.as_view()),
     path('sensors/<pk>/', RetrieveUpdateSensor.as_view()),
]
