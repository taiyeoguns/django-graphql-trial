import graphene
from graphene_django import DjangoObjectType

from .models import Department, Employee


class DepartmentType(DjangoObjectType):
    """Type for Department Model

    Arguments:
        DjangoObjectType
    """
    class Meta:
        model = Department
        exclude_fields = "uuid"

    id = graphene.UUID()

    def resolve_id(self, info, **kwargs):
        return self.uuid


class EmployeeType(DjangoObjectType):
    """Type for Employee Model

    Arguments:
        DjangoObjectType
    """
    class Meta:
        model = Employee
        exclude_fields = "uuid"

    id = graphene.UUID()

    def resolve_id(self, info, **kwargs):
        return self.uuid


class Query(graphene.ObjectType):
    """GraphQL Query

    Arguments:
        graphene
    """
    departments = graphene.List(DepartmentType)
    employees = graphene.List(EmployeeType)

    def resolve_departments(self, info, **kwargs):
        return Department.objects.all()

    def resolve_employees(self, info, **kwargs):
        return Employee.objects.all()
