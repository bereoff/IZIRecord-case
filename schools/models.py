from django.db import models

from utils.base_model import ModelUUIDBased


class School(ModelUUIDBased):
    name = models.CharField(max_length=255, blank=True, null=True)
    maximum_capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
