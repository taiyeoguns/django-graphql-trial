from mixer.backend.django import mixer

from base.models import Department, Employee
from gql.schema import schema


def test_department_list(db):
    """
    Test that departments can be retrieved
    """

    dept1, dept2 = mixer.cycle(2).blend(Department)

    response = schema.execute(
        """
        query {
            departments {
                id
                name
            }
        }
        """
    )

    departments = response.data["departments"]

    assert len(departments) == 2
    assert str(dept1.uuid) in departments[0].values()
    assert str(dept2.name) in departments[1].values()
    assert not response.errors


def test_department_create(db):
    """
    Test that new department can be created
    """

    name = "New Department"

    mutation = f"""
        mutation {{
            createDepartment(name: "{name}")
            {{
                id
                name
                createdAt
            }}
        }}
        """

    response = schema.execute(mutation)

    department = response.data["createDepartment"]

    db_dept = Department.objects.first()

    assert not response.errors
    assert Department.objects.count() == 1
    assert department["name"] == name
    assert str(db_dept.uuid) == department["id"]


def test_department_update(db):
    """
    Test that existing department can be updated
    """

    dept = mixer.blend(Department, name="Dept 1")

    new_name = "Dept One"

    mutation = f"""
        mutation {{
            updateDepartment(
                id: "{str(dept.uuid)}"
                name: "{new_name}"
            )
            {{
                id
                name
            }}
        }}
        """

    response = schema.execute(mutation)

    department = response.data["updateDepartment"]

    db_dept = Department.objects.get(uuid=dept.uuid)

    assert not response.errors
    assert department["name"] == new_name
    assert department["id"] == str(dept.uuid)
    assert db_dept is not None
    assert db_dept.name == new_name


def test_department_delete(db):
    """
    Test that department can be deleted
    """

    dept = mixer.blend(Department)

    mutation = f"""
        mutation {{
            deleteDepartment(
                id: "{str(dept.uuid)}"
            )
            {{
                id
            }}
        }}
        """

    response = schema.execute(mutation)

    department = response.data["deleteDepartment"]

    assert not response.errors
    assert department["id"] == str(dept.uuid)
    assert Department.objects.count() == 0


def test_employee_list_only(db):
    """
    Test that employees can be retrieved
    """
    emp1, emp2 = mixer.cycle(2).blend(Employee)

    query = f"""
        query {{
            employees {{
                id
                firstName
                lastName
                createdAt
            }}
        }}
        """

    response = schema.execute(query)

    employees = response.data["employees"]

    assert len(employees) == 2
    assert str(emp1.uuid) in employees[0].values()
    assert str(emp2.last_name) in employees[1].values()
    assert not response.errors


def test_employee_list_with_department(db):
    """
    Test that employees can be retrieved with related department
    """

    dept = mixer.blend(Department)
    emp = mixer.blend(Employee, department=dept)

    query = f"""
        query {{
            employees {{
                id
                firstName
                lastName
                createdAt
                department {{
                    id
                    name
                }}
            }}
        }}
        """

    response = schema.execute(query)

    employees = response.data["employees"]
    department = employees[0]["department"]

    assert not response.errors
    assert str(emp.uuid) in employees[0].values()
    assert str(dept.uuid) in department.values()
    assert department["id"] == str(emp.department.uuid)
