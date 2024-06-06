from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import CarFilter, MarkaFilter


class MarkaViewSet(viewsets.ModelViewSet):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = MarkaFilter
    permission_classes = [permissions.IsAuthenticated]


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CarFilter
    search_fields = ['country']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializers
    permission_classes = [permissions.IsAuthenticated]