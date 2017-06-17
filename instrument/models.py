# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from lims_rest import settings


class User(AbstractUser):
    phone = models.CharField(max_length=64, blank=True, null=True)

    def __unicode__(self):
        return self.last_name + '' + self.first_name or str(self.username)


class Department(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Instrument(models.Model):
    INSTRUMENT_STATUS_CHOICES = (
        ('R', 'ready'),
        ('O', 'occupied'),
        ('U', 'unavailable')
    )
    name = models.CharField(max_length=256)
    # todo admin m2m
    status = models.CharField(max_length=64, choices=INSTRUMENT_STATUS_CHOICES, default='R')
    department = models.ForeignKey(Department, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to=settings.UPLOAD_FOLDER, max_length=256)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Reservation(models.Model):
    instrument = models.ForeignKey(Instrument)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
