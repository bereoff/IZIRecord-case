from django.db import models

from utils.base_model import ModelUUIDBased


class School(ModelUUIDBased):
    name = models.CharField(max_length=255, blank=True, null=True)
    maximum_capacity = models.IntegerField(blank=True, null=True)

    def _str_(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
