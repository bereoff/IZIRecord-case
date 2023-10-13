import factory

from person.models import Person, Student
from schools.models import School


class SchoolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = School

    name = "test_name"


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = "test_first_name"
    last_name = "test_last_name"


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = "test_first_name"
    last_name = "test_last_name"
    school = factory.SubFactory(SchoolFactory)
