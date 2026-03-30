from rest_framework.serializers import ModelSerializer

from apps.courses.models import Category, Tag, Author


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


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "full_name", "age", "gender", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
