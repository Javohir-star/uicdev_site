from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.common.apis.serializers import (
    EducationSerializer,
)
from apps.common.models import Education


class EducationListCreateAPIView(ListCreateAPIView):
    queryset = Education.objects.all().order_by("name")
    serializer_class = EducationSerializer


class EducationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
