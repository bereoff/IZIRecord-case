import pytest

from ..models import School


@pytest.mark.django_db
def test_str_method():
    School.objects.create(name="School 1", maximum_capacity=100)

    obj = School.objects.get()
    assert str(obj) == "School 1"
