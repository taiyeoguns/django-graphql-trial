from secrets import choice

from django.core.management.base import BaseCommand
from django.utils import timezone
from mixer.backend.django import mixer

from base.models import Department, Employee


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def _get_user(self):
        fname = mixer.faker.first_name()
        lname = mixer.faker.last_name()
        email = f"{fname}.{lname}@graphqlapi.local".lower()
        dob = mixer.faker.date()

        return {"fname": fname, "lname": lname, "email": email, "dob": dob}

    def _get_department(self):
        depts = ("Accounts", "Staffing", "Marketing", "Design", "Development", "Testing")

        return f"{mixer.faker.word()} {choice(depts)}".title()

    def _clear(self):
        self.stdout.write("Clearing data")

        Employee.objects.all().delete()
        Department.objects.all().delete()

    def add_arguments(self, parser):
        parser.add_argument(
            "--num", type=int, default=10, help="Number of items to create"
        )

    def handle(self, *args, **options):

        self._clear()  # clear existing table entries

        self.stdout.write("Starting...")

        self.stdout.write("Seeding Departments")

        # set bounds not less than 5 or greater than 100
        if options["num"] < 5:
            options["num"] = 5

        if options["num"] > 100:
            options["num"] = 100

        for i in range(options["num"]):

            if i < round(0.4 * options["num"]) - 1:
                mixer.blend(
                    Department,
                    name=self._get_department(),
                    created_at=mixer.faker.date_time_between(
                        start_date="-1w", tzinfo=timezone.get_current_timezone()
                    ),
                )

        # seed shifts
        self.stdout.write("Seeding Employees")

        for i in range(options["num"]):

            # seed users
            _user = self._get_user()

            mixer.blend(
                Employee,
                first_name=_user.get("fname"),
                last_name=_user.get("lname"),
                email=_user.get("email"),
                dob=_user.get("dob"),
                department=mixer.SELECT,
                created_at=mixer.faker.date_time_between(
                    start_date="-1w", tzinfo=timezone.get_current_timezone()
                ),
            )

        self.stdout.write("Done.")
