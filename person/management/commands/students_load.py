from django.core.management import BaseCommand

from person.models import Student
from schools.models import School


class Command(BaseCommand):
    help = 'Initial test load data'

    def handle(self, *args, **kwargs):
        try:
            schools = [
                School(name="New York School", maximum_capacity=100),  # NOQA
                School(name="London School", maximum_capacity=100),  # NOQA
                School(name="Tokyo School", maximum_capacity=100),  # NOQA
                School(name="Sydney School", maximum_capacity=100),  # NOQA
                School(name="Montreal School", maximum_capacity=100),  # NOQA
                School(name="Rio de Janeiro School", maximum_capacity=100),  # NOQA
                School(name="Buenos Aires School", maximum_capacity=100)  # NOQA
            ]
            School.objects.bulk_create(schools)

            school_us = School.objects.get(name="New York School")
            school_en = School.objects.get(name="London School")
            school_jp = School.objects.get(name="Tokyo School")
            school_aus = School.objects.get(name="Sydney School")
            school_ca = School.objects.get(name="Montreal School")
            school_br = School.objects.get(name="Rio de Janeiro School")
            school_ar = School.objects.get(name="Buenos Aires School")

            students = [
            {"first_name": "Axel", "last_name": "Foley", "grade": "10-A", "school": school_us},  # NOQA
            {"first_name": "Harry", "last_name": "Potter", "grade": "10-A", "school": school_en},  # NOQA
            {"first_name": "Shigeru", "last_name": "Miyamoto", "grade": "10-A", "school": school_jp},  # NOQA
            {"first_name": "Cate", "last_name": "Blanchett", "grade": "10-A", "school": school_aus},  # NOQA
            {"first_name": "Seth", "last_name": "Rogen", "grade": "10-A", "school": school_ca},  # NOQA
            {"first_name": "Tom", "last_name": "Jobim", "grade": "10-A", "school": school_br},  # NOQA
            {"first_name": "Diego", "last_name": "Maradona", "grade": "10-A", "school": school_ar},  # NOQA
            ]

            for student in students:
                Student.objects.create(**student)

            print(54 * "#" + " " + " Students Successefully Created" + " " + 54 * "#")   # NOQA
            print(54 * "#" + " " + " Schools Successefully Created" + 2 * " " + 54 * "#")   # NOQA
        except Exception as e:
            raise e
