# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
from django.shortcuts import render

from instrument import models


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass
