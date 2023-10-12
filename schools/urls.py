from django.urls import path

from .views import (SchoolDestroyView, SchoolListCreateView,
                    SchoolRetrieveView, SchoolsSearchListView)

urlpatterns = [
    path("", SchoolListCreateView.as_view(), name="list_create_schools"),  # NOQA
    path("search/", SchoolsSearchListView.as_view(), name="schools_search"),  # NOQA
    path("school/<uuid:pk>/", SchoolDestroyView.as_view(), name="school_delete"),  # NOQA
    path("detail/<uuid:pk>/", SchoolRetrieveView.as_view(), name="school_detail"),  # NOQA
]
