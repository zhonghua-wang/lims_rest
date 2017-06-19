from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from instrument import models


class UserNode(DjangoObjectType):
    class Meta:
        model = models.User
        interfaces = (relay.Node,)


class DepartmentNode(DjangoObjectType):
    class Meta:
        model = models.Department
        interfaces = (relay.Node,)


class InstrumentNode(DjangoObjectType):
    class Meta:
        model = models.Instrument
        interfaces = (relay.Node,)


class Query(AbstractType):
    instrument = relay.Node.Field(InstrumentNode)
    all_instruments = DjangoFilterConnectionField(InstrumentNode)
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
    department = relay.Node.Field(DepartmentNode)
    all_departments = DjangoFilterConnectionField(DepartmentNode)
