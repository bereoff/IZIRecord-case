import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from ..models import School


class SchoolCreateRecordTestCase(APITestCase):

    """
    Test to create School object.
    """

    def setUp(self):
        self.client = APIClient()
        self.data = [{
            "name": "test school",
            "maximum_capacity": 400
        }]
        self.url = "/api/v1/schools/available-new/"

    def test_create_school(self):
        """
        test SchoolListCreateView create method
        """
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 1)
        self.assertEqual(School.objects.get().name, self.data[0]["name"])


class SchoolGetRecordsTestCase(APITestCase):

    """
    Test to retrieve School objects.
    """

    def setUp(self):
        self.client = APIClient()
        School.objects.create(name="School 1", maximum_capacity=100)
        School.objects.create(name="School 2", maximum_capacity=200)
        School.objects.create(name="School 3", maximum_capacity=300)
        School.objects.create(name="School 4", maximum_capacity=400)
        School.objects.create(name="School 5", maximum_capacity=500)
        self.schools = School.objects.all()
        self.school_5 = School.objects.get(name="School 5")
        self.pk = School.objects.get(name="School 5").pk

    def test_get_all_items(self):
        """
        test SchoolListCreateView list method
        """
        self.assertEqual(self.schools.count(), 5)
        response = self.client.get("/api/v1/schools/available-new/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_item_by_term(self):
        """
        test SchoolsSearchListView retrieve method
        """
        response = self.client.get(
            "/api/v1/schools/by_name/", {"term": "School 5"})
        self.assertContains(response, self.school_5.name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SchoolDeleteRecordsTestCase(APITestCase):

    """
    Test to delete School objects
    """

    def setUp(self):
        self.client = APIClient()
        School.objects.create(name="School 6", maximum_capacity=100)
        self.school_id = School.objects.get(name="School 6").pk

    def test_delete_item_by_pk(self):
        """
        test SchoolsSearchListView retrieve method
        """

        response = self.client.delete(
            reverse("school_delete", kwargs={"pk": self.school_id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SchoolUpdateRecordsTestCase(APITestCase):

    """
    Test to update School objects
    """

    def setUp(self):
        self.school = School.objects.create(
            name="Valencia School", maximum_capacity=400)

        self.valid_payload = {
            "name": 'Muffy',
            "maximum_capacity": 600
        }

    def test_update_school(self):
        """
        test SchoolUpdateView retrieve method
        """
        response = self.client.put(
            reverse('school_update', kwargs={'pk': self.school.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
