from django.urls import path
from .views import car_cost_view

urlpatterns = [
    path('', car_cost_view, name='car-cost'),
]
