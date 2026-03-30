from rest_framework.serializers import ModelSerializer

from apps.accounts.models import Country, Region, Author, User


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


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "full_name", "age", "gender", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "phone", "password", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def save(self, **kwargs):
        user = User(
            phone=self.validated_data["phone"],
            password=self.validated_data["password"],
            is_active=False,
            is_deleted=False,
        )
        user.save()
        return user


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "phone",
            "first_name",
            "last_name",
            "avatar",
            "bio",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
