from rest_framework import serializers
from instrument import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        exclude = []


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Department
        exclude = []


class InstrumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Instrument
        exclude = []


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Reservation
        exclude = []
