from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import School


class SchoolTestCase(APITestCase):

    """
    Test create School
    """

    def setUp(self):
        self.client = APIClient()
        self.data = [{
            "name": "test school",
            "maximum_capacity": 400
        }]
        self.url = "/api/v1/schools/available-new/"

    def test_create_contact(self):
        '''
        test ContactViewSet create method
        '''
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 1)
        self.assertEqual(School.objects.get().name, self.data[0]["name"])
