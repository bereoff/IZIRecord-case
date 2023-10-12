from django.urls import include, path

from .views import (SchoolDestroyAPIView, SchoolListCreateView,
                    SchoolRetrieveAPIView)

urlpatterns = [
    path("", SchoolListCreateView.as_view(), name="list_create_schools"),  # NOQA
    path("school/<uuid:pk>/", SchoolDestroyAPIView.as_view(), name="school_delete"),  # NOQA
    path("detail/<uuid:pk>/", SchoolRetrieveAPIView.as_view(), name="school_detail"),  # NOQA
]
