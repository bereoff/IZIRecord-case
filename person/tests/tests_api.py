from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from schools.models import School

from ..models import Student


class StudentCreateOneRecordTestCase(APITestCase):

    """
    Test to create Students objects.
    """

    def setUp(self):
        self.client = APIClient()
        school_1 = School.objects.create(name="School 1", maximum_capacity=100)
        self.data = [{
            "first_name": "Name 1",
            "last_name": "Lastname 1",
            "school": school_1.pk
        }]
        self.url = "/api/v1/person/student/"

    def test_create_student(self):
        """
        test StudentCreateView create method
        """
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().first_name, self.data[0]["first_name"])  # NOQA


class StudentCreateMultipleRecordTestCase(APITestCase):

    """
    Test to create multiple Students objects according to
    business rule.
    """

    def setUp(self):
        self.client = APIClient()
        school_1 = School.objects.create(name="School 1", maximum_capacity=2)
        self.data = [
            {"first_name": "Name 1", "last_name": "Lastname 1", "school": school_1.pk},  # NOQA
            {"first_name": "Name 2", "last_name": "Lastname 2", "school": school_1.pk},  # NOQA
            {"first_name": "Name 3", "last_name": "Lastname 3", "school": school_1.pk}]  # NOQA

        self.url = "/api/v1/person/student/"

    def test_create_multiple_students(self):
        """
        test StudentCreateView create method
        """
        data = self.data
        response = self.client.post(self.url, data)
        students = response.data
        student_1 = students[0]
        student_2 = students[1]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)
        self.assertEqual(student_1["first_name"], self.data[0]["first_name"])  # NOQA
        self.assertEqual(student_2["first_name"], self.data[1]["first_name"])  # NOQA


class StudentNotCreateRecordTestCase(APITestCase):

    """
    Test to create multiple Students objects according to
    business rule.
    """

    def setUp(self):
        self.client = APIClient()
        school_1 = School.objects.create(name="School 1", maximum_capacity=0)
        self.data = [
            {"first_name": "Name 1", "last_name": "Lastname 1", "school": school_1.pk}]  # NOQA
        self.url = "/api/v1/person/student/"

    def test_maximum_capacity_reached(self):
        """
        test StudentCreateView create method
        """
        student = self.data
        response = self.client.post(self.url, student)
        data = response.data
        self.assertEqual(Student.objects.count(), 0)
        self.assertEqual(data["msg"], "the school has reached its maximum capacity")  # NOQA


class StudentGetRecordsTestCase(APITestCase):

    """
    Test to retrieve Student objects.
    """

    def setUp(self):
        self.client = APIClient()
        school = School.objects.create(name="School 1", maximum_capacity=100)
        Student.objects.create(first_name="Name 1",
                               last_name="Lastname 1", school=school)
        Student.objects.create(first_name="Name 2",
                               last_name="Lastname 2", school=school)
        Student.objects.create(first_name="Name 3",
                               last_name="Lastname 3", school=school)
        Student.objects.create(first_name="Name 4",
                               last_name="Lastname 4", school=school)
        Student.objects.create(first_name="Name 5",
                               last_name="Lastname 5", school=school)

        self.student_3 = Student.objects.get(first_name="Name 3")
        self.student_5 = Student.objects.get(first_name="Name 5")

    def test_get_item_by_firstname(self):
        """
        test StudentsSearchListView retrieve method
        """
        response = self.client.get(
            "/api/v1/person/student/by_name/", {"first_name": "Name 3"})
        data = response.data
        self.assertEqual(data[0]["first_name"], self.student_3.first_name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_item_by_lastname(self):
        """
        test StudentsSearchListView retrieve method
        """
        response = self.client.get(
            "/api/v1/person/student/by_name/", {"last_name": "Lastname 5"})
        data = response.data
        self.assertEqual(data[0]["last_name"], self.student_5.last_name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class StudentDeleteRecordsTestCase(APITestCase):

    """
    Test to delete Student objects
    """

    def setUp(self):
        self.client = APIClient()
        school = School.objects.create(name="School 1", maximum_capacity=100)
        Student.objects.create(
            first_name="Name 1",
            last_name="Lastname 1",
            school=school
        )
        self.student_id = Student.objects.get(first_name="Name 1").pk

    def test_delete_item_by_pk(self):
        """
        test StudentDestroyView retrieve method
        """

        response = self.client.delete(
            reverse("student_delete", kwargs={"pk": self.student_id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
