# from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Student


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ["created_at", "updated_at"]
