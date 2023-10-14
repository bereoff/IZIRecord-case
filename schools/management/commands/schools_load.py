from django.core.management import BaseCommand

from schools.models import School


class Command(BaseCommand):

    help = 'Initial test load data'

    def handle(self, *args, **kwargs):
        try:
            schools = [
                School(name="Barcelona School", maximum_capacity=100),  # NOQA
                School(name="Madrid School", maximum_capacity=100),  # NOQA
                School(name="Lisbon School", maximum_capacity=100),  # NOQA
                School(name="Milan School", maximum_capacity=100),  # NOQA
                School(name="Berlin School", maximum_capacity=100),  # NOQA
                School(name="Paris School", maximum_capacity=100),  # NOQA
                School(name="Paris School", maximum_capacity=100),  # NOQA
            ]
            School.objects.bulk_create(schools)

            print(54 * "#" + " " + " Schools Successefully Created" + 2 * " " + 54 * "#")   # NOQA
        except Exception as e:
            raise e
