from django.db import models

from schools.models import School
from utils.base_model import ModelUUIDBased


class Person(ModelUUIDBased):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    grade = models.CharField(max_length=50, blank=True, null=True)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='students_school')
