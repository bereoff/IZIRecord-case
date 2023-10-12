from rest_framework import status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveAPIView)
from rest_framework.response import Response

from person import models, serializers


class StudentCreateView(CreateAPIView):

    queryset = models.School.objects.all()
    serializer_class = serializers.StudentsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)  # NOQA
