import graphene
from graphene_django.debug import DjangoDebug
import instrument.schema


class Query(instrument.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
