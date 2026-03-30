from rest_framework.serializers import ModelSerializer

from apps.common.models import Country, Education, Region, Author, Category, Tag, Course


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
