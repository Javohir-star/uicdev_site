from rest_framework.serializers import ModelSerializer

from apps.courses.models import Enrollment


class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            "id",
            "user",
            "course",
            "started_at",
            "finished_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
