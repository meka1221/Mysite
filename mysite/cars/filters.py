from django_filters.rest_framework import FilterSet
from .models import Car, Marka


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'model': ['exact'],
            'price': ['gt', 'lt'],
            'marka': ['exact']
        }


class MarkaFilter(FilterSet):
    class Meta:
        model = Marka
        fields = {
            'title_marka': ['exact']
        }