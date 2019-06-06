import graphene

import base.schema


class Query(base.schema.Query, graphene.ObjectType):
    pass


class Mutation(base.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
