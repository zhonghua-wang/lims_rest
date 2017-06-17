# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from instrument import models
from instrument import serializers

# #   api root
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'user': reverse('user-list', request=request, format=format),
#         'instrument': reverse('instrument-list', request=request, format=format)
#     })


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = models.Instrument.objects.all()
    serializer_class = serializers.InstrumentSerializer
    filter_fields = (
        'status', 'department', 'location'
    )


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer
