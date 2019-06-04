import graphene
from graphene_django import DjangoObjectType

from .models import Department


class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department
        exclude_fields = "uuid"

    id = graphene.UUID()

    def resolve_id(self, info, **kwargs):
        return self.uuid


class Query(graphene.ObjectType):
    departments = graphene.List(DepartmentType)

    def resolve_departments(self, info, **kwargs):
        return Department.objects.all()
