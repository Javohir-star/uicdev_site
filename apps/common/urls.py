from django.urls import path

from apps.common.apis import (
    CountryListCreateAPIView,
    CountryRetrieveUpdateDestroyAPIView,
    RegionListCreateAPIView,
    RegionRetrieveUpdateDestroyAPIView,
    EducationListCreateAPIView,
    EducationRetrieveUpdateDestroyAPIView,
    AuthorListCreateAPIView,
    AuthorRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    TagListCreateAPIView,
    TagRetrieveUpdateDestroyAPIView,
    CourseListCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("countries/", CountryListCreateAPIView.as_view(), name="country-list"),
    path(
        "countries/<int:pk>/",
        CountryRetrieveUpdateDestroyAPIView.as_view(),
        name="country-detail",
    ),
    path("regions/", RegionListCreateAPIView.as_view(), name="region-list"),
    path(
        "regions/<int:pk>/",
        RegionRetrieveUpdateDestroyAPIView.as_view(),
        name="region-detail",
    ),
    path("educations/", EducationListCreateAPIView.as_view(), name="education-list"),
    path(
        "educations/<int:pk>/",
        EducationRetrieveUpdateDestroyAPIView.as_view(),
        name="education-detail",
    ),
    path("authors/", AuthorListCreateAPIView.as_view(), name="author-list"),
    path(
        "authors/<int:pk>/",
        AuthorRetrieveUpdateDestroyAPIView.as_view(),
        name="author-detail",
    ),
    path("categorys/", CategoryListCreateAPIView.as_view(), name="category-list"),
    path(
        "categorys/<int:pk>/",
        CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category-detail",
    ),
    path("tags/", TagListCreateAPIView.as_view(), name="tag-list"),
    path(
        "tags/<int:pk>/",
        TagRetrieveUpdateDestroyAPIView.as_view(),
        name="tag-detail",
    ),
    path("courses/", CourseListCreateAPIView.as_view(), name="course-list"),
    path(
        "courses/<int:pk>/",
        CourseRetrieveUpdateDestroyAPIView.as_view(),
        name="course-detail",
    ),
]
