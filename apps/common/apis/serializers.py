from rest_framework.serializers import ModelSerializer

from apps.common.models import Country, Education, Region, Author, Category, Tag, Course


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "full_name", "age", "gender", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "start_date", "end_date", "teacher", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
