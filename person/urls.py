from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (StudentCreateView, StudentDestroyView,
                    StudentsRetrieveListView, StudentsSearchListView)

router = DefaultRouter()

router.register("students", StudentsRetrieveListView,
                basename="StudentsRetrieveList")

urlpatterns = [
    path("", include(router.urls)),
    path("student/", StudentCreateView.as_view(), name="students_creation"),  # NOQA
    path("student/search/", StudentsSearchListView.as_view(), name="students_search"),  # NOQA
    path("student/<uuid:pk>/", StudentDestroyView.as_view(), name="student_delete"),  # NOQA
]
