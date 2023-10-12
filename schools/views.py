from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import (DestroyAPIView, ListCreateAPIView,
                                     RetrieveAPIView)
from rest_framework.response import Response

from schools import models, serializers


class SchoolListCreateView(ListCreateAPIView):

    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolsSerializer

    def get_queryset(self):
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)  # NOQA


class SchoolDestroyAPIView(DestroyAPIView):

    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolsSerializer

    # TODO - give a successfully message
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class SchoolRetrieveAPIView(RetrieveAPIView):

    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolDetailSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
