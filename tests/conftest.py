from pytest_factoryboy import register

from .factories import PersonFactory, SchoolFactory, StudentFactory

register(PersonFactory)
register(StudentFactory)
register(SchoolFactory)
