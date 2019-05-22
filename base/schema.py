import graphene
from graphene_django import DjangoObjectType

from .models import Department


class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department


class Query(graphene.ObjectType):
    departments = graphene.List(DepartmentType)

    def resolve_departments(self, info, **kwargs):
        return Department.objects.all()
