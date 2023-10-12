from django.shortcuts import get_object_or_404
from rest_framework import serializers

from person.models import Student
from person.serializers import StudentsSerializer

from .models import School


class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SchoolDetailSerializer(serializers.ModelSerializer):

    students = StudentsSerializer(many=True, source="students_school")

    class Meta:
        model = School
        fields = "__all__"
