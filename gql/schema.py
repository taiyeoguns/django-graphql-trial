import graphene

import base.schema


class Query(base.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
