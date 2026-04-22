from django.urls import path

from apps.courses.views import (
    CategoryCreateAPIView,
    CategoryDeleteAPIView,
    CategoryListAPIView,
    CategoryRetrieveAPIView,
    CategoryUpdateAPIView,
    CourseListAPIView,
    CourseRetrieveAPIView,
    TagCreateAPIView,
    TagDeleteAPIView,
    TagListAPIView,
    TagRetrieveAPIView,
    TagUpdateAPIView,
    EnrollmentCreateAPIView,
    EnrollmentDeleteAPIView,
    EnrollmentListAPIView,
    EnrollmentRetrieveAPIView,
    EnrollmentUpdateAPIView,

)

urlpatterns = [
    path("tags/", TagListAPIView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateAPIView.as_view(), name="tag-create"),
    path("tags/<int:pk>/", TagRetrieveAPIView.as_view(), name="tag-retrieve"),
    path("tags/<int:pk>/update/", TagUpdateAPIView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteAPIView.as_view(), name="tag-delete"),
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("categories/create/", CategoryCreateAPIView.as_view(), name="category-create"),
    path(
        "categories/<int:pk>/",
        CategoryRetrieveAPIView.as_view(),
        name="category-retrieve",
    ),
    path(
        "categories/<int:pk>/update/",
        CategoryUpdateAPIView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        CategoryDeleteAPIView.as_view(),
        name="category-delete",
    ),
    path("enrollments/", EnrollmentListAPIView.as_view(), name="enrollment-list"),
    path("enrollments/create/", EnrollmentCreateAPIView.as_view(), name="enrollment-create"),
    path("enrollments/<int:pk>/", EnrollmentRetrieveAPIView.as_view(), name="enrollment-retrieve"),
    path("enrollments/<int:pk>/update/", EnrollmentUpdateAPIView.as_view(), name="enrollment-update"),
    path("enrollments/<int:pk>/delete/", EnrollmentDeleteAPIView.as_view(), name="enrollment-delete"),
]
