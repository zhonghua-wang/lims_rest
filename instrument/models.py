# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from lims_rest import settings


class Group(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class User(models.Model):
    user = models.OneToOneField("auth.User")
    group = models.ForeignKey(Group, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)

    def __unicode__(self):
        return self.user.name

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
    admin = models.ForeignKey(User)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Reservation(models.Model):
    instrument = models.ForeignKey(Instrument)
    user = models.ForeignKey(User)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
