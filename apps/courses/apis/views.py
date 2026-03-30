from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.courses.apis.serializers import (
    AuthorSerializer,
    CategorySerializer,
    TagSerializer,
)
from apps.courses.models import Author, Category, Tag


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all().order_by("name")
    serializer_class = TagSerializer


class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all().order_by("full_name")
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
