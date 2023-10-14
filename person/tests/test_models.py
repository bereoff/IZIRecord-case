import pytest

from schools.models import School

from ..models import Student


@pytest.mark.django_db
def test_str_method():
    school_1 = School.objects.create(name="School 1", maximum_capacity=100)
    Student.objects.create(
        first_name="Name 1",
        last_name="Lastname 1",
        school=school_1
    )
    obj = Student.objects.get()
    assert str(obj) == "Name 1 Lastname 1"
