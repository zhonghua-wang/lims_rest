from rest_framework import serializers
from instrument import models


class UserSerializer(serializers.ModelSerializer):
   # profile = serializers.RelatedField(source='user', read_only=True)
    class Meta:
        model = models.User
        exclude = []


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        exclude = []


class InstrumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Instrument
        exclude = []


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        exclude = []
