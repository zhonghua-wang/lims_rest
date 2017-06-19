from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import django_filters
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


class InstrumentFilter(django_filters.FilterSet):
    department = django_filters.UUIDFilter

    class Meta:
        model = models.Instrument
        exclude = ['image']


class Query(AbstractType):
    instrument = relay.Node.Field(InstrumentNode)
    all_instruments = DjangoFilterConnectionField(
        InstrumentNode,
        filterset_class=InstrumentFilter
    )
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
    department = relay.Node.Field(DepartmentNode)
    all_departments = DjangoFilterConnectionField(DepartmentNode)
