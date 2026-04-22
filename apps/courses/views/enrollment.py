from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from apps.courses.models import Enrollment
from apps.courses.serializers import EnrollmentSerializer


class EnrollmentCreateAPIView(CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentListAPIView(ListAPIView):
    queryset = Enrollment.objects.all().order_by("id")
    serializer_class = EnrollmentSerializer


class EnrollmentRetrieveAPIView(RetrieveAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentUpdateAPIView(UpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentDeleteAPIView(DestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
