from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.accounts.apis.serializers import (
    AuthorSerializer,
    CountrySerializer,
    RegionSerializer,
    UserRegisterSerializer,
)
from apps.accounts.models import Author, Country, Region, User


class CountryListCreateAPIView(ListCreateAPIView):
    queryset = Country.objects.all().order_by("name")
    serializer_class = CountrySerializer


class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RegionListCreateAPIView(ListCreateAPIView):
    queryset = Region.objects.all().order_by("name")
    serializer_class = RegionSerializer


class RegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all().order_by("full_name")
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserRegisterAPIView(GenericAPIView):
    queryset = User.objects.filter(is_active=True, is_deleted=False)
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if User.objects.filter(phone=serializer.validated_data["phone"]).exists():
            raise ValidationError("User already exists")

        user = serializer.save()
        return Response(UserRegisterSerializer(user).data)


class UserProfileAPIView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True, is_deleted=False).select_related(
        "avatar"
    )
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_object(self):
        return self.request.user
