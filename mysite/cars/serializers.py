from rest_framework import serializers
from .models import *


class MarkaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class ModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class BetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'

