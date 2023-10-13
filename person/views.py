import json

from django.shortcuts import get_object_or_404
from rest_framework import generics, response, status, views, viewsets

from person import models, serializers
from schools.models import School


class StudentsRetrieveListView(viewsets.ViewSet):
    serializer_class = serializers.StudentsSerializer

    def list(self, request):
        queryset = models.Student.objects.all()
        serializer = serializers.StudentsSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = serializers.StudentsSerializer(student)
        return response.Response(serializer.data)


class StudentCreateView(generics.CreateAPIView):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentsSerializer

    def create(self, request, *args, **kwargs):
        students = json.loads(self.request.body)

        school_id = set([student.get("school") for student in students]).pop()
        school = get_object_or_404(School, id=school_id)
        enrolled_students = models.Student.objects.filter(
            school=school.id).count()

        available_vacancies = school.maximum_capacity - enrolled_students

        if available_vacancies == 0:
            return response.Response(data={"msg": "the school has reached its maximum capacity"}, status=status.HTTP_200_OK)  # NOQA

        chosen_students = students[:available_vacancies]

        serializer = self.get_serializer(
            data=chosen_students, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)  # NOQA


class StudentDestroyView(generics.DestroyAPIView):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentsSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response(data={"msg": "successefully deleted"}, status=status.HTTP_204_NO_CONTENT)


class StudentsSearchListView(views.APIView):
    serializer_class = serializers.StudentsSerializer

    def get(self, request):
        queryset = models.Student.objects.all()
        request_path = self.request.get_full_path()
        if "first_name" in request_path:
            first_name = self.request.query_params.get("first_name")
            if first_name is not None:
                queryset = queryset.filter(first_name__icontains=first_name)
                return response.Response(serializers.StudentsSerializer(queryset, many=True).data)
        elif "last_name" in request_path:
            last_name = self.request.query_params.get("last_name")
            if last_name is not None:
                queryset = queryset.filter(last_name__icontains=last_name)
                return response.Response(serializers.StudentsSerializer(queryset, many=True).data)

        return response.Response(data={"msg": "no terms were given"}, status=status.HTTP_400_BAD_REQUEST)
