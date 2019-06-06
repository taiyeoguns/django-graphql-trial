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


class CreateDepartment(graphene.Mutation):
    """Creates a new department

    Arguments:
        graphene
    """

    id = graphene.UUID()
    name = graphene.String()
    created_at = graphene.DateTime()

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        department = Department.objects.create(name=name)

        return CreateDepartment(
            id=department.uuid, name=department.name, created_at=department.created_at
        )


class UpdateDepartment(graphene.Mutation):
    """Updates an existing department

    Arguments:
        graphene
    """

    id = graphene.UUID()
    name = graphene.String()

    class Arguments:
        id = graphene.UUID()
        name = graphene.String()

    def mutate(self, info, id, name):
        department = Department.objects.get(uuid=id)
        department.name = name
        department.save()

        return UpdateDepartment(id=department.uuid, name=department.name)


class DeleteDepartment(graphene.Mutation):
    """Deletes a department

    Arguments:
        graphene
    """

    id = graphene.UUID()

    class Arguments:
        id = graphene.UUID()

    def mutate(self, info, id):
        Department.objects.get(uuid=id).delete()

        return DeleteDepartment(id=id)


class Mutation(graphene.ObjectType):
    """Mutations

    Arguments:
        graphene
    """

    create_department = CreateDepartment.Field()
    delete_department = DeleteDepartment.Field()
    update_department = UpdateDepartment.Field()
