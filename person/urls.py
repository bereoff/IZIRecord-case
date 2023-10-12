from django.urls import path

from .views import StudentCreateView

urlpatterns = [
    path("student/", StudentCreateView.as_view(), name="student_creation"),  # NOQA
    # path("school/<uuid:pk>/", SchoolDestroyAPIView.as_view(), name="school_delete"),  # NOQA
    # path("school/detail/<uuid:pk>/", SchoolRetrieveAPIView.as_view(), name="school_detail"),  # NOQA
]
