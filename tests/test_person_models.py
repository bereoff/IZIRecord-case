import pytest

pytestmark = pytest.mark.django_db


class TestPersonModels:
    def test_str_method(self, person_factory):
        obj = person_factory(first_name="test_first_name",
                             last_name="test_last_name")

        assert obj.__str__() == "test_first_name test_last_name"


class TestStudentModels:
    def test_str_method(self, student_factory):
        obj = student_factory()

        assert obj.__str__() == "test_first_name test_last_name"
