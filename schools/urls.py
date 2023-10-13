from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (SchoolDestroyView, SchoolListCreateView,
                    SchoolRetrieveListView, SchoolsSearchListView)

router = DefaultRouter()

router.register("details", SchoolRetrieveListView,
                basename="SchoolRetrieveList")

urlpatterns = [
    path("", include(router.urls)),
    path("available-new/", SchoolListCreateView.as_view(), name="list_create_schools"),  # NOQA
    path("by_name/", SchoolsSearchListView.as_view(), name="schools_search"),  # NOQA
    path("school/<uuid:pk>/", SchoolDestroyView.as_view(), name="school_delete"),  # NOQA
]
