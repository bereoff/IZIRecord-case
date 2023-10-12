from rest_framework import generics, response, status

from schools import models, serializers


class SchoolListCreateView(generics.ListCreateAPIView):

    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolsSerializer

    def get_queryset(self):
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)  # NOQA


class SchoolsSearchListView(generics.ListAPIView):

    serializer_class = serializers.SchoolsSerializer

    def get_queryset(self):

        queryset = models.School.objects.all()
        term = self.request.query_params.get("term")
        if term is not None:
            queryset = queryset.filter(name__icontains=term)
        return queryset


class SchoolDestroyView(generics.DestroyAPIView):

    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolsSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response(data={"msg": "successefully deleted"}, status=status.HTTP_204_NO_CONTENT)


class SchoolRetrieveView(generics.RetrieveAPIView):

    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolDetailSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
