import pytest

pytestmark = pytest.mark.django_db


class TestSchoolModels:
    def test_str_method(self, school_factory):
        obj = school_factory(name="test_name")

        assert obj.__str__() == "test_name"
