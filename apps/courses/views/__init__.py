from .tag import (
    TagCreateAPIView,
    TagListAPIView,
    TagRetrieveAPIView,
    TagUpdateAPIView,
    TagDeleteAPIView,
)
from .category import (
    CategoryCreateAPIView,
    CategoryListAPIView,
    CategoryRetrieveAPIView,
    CategoryUpdateAPIView,
    CategoryDeleteAPIView,
)
from .course import (
    CourseCreateAPIView,
    CourseListAPIView,
    CourseRetrieveAPIView,
    CourseUpdateAPIView,
    CourseDeleteAPIView,
)

__all__ = [
    "TagCreateAPIView",
    "TagListAPIView",
    "TagRetrieveAPIView",
    "TagUpdateAPIView",
    "TagDeleteAPIView",
    "CategoryCreateAPIView",
    "CategoryListAPIView",
    "CategoryRetrieveAPIView",
    "CategoryUpdateAPIView",
    "CategoryDeleteAPIView",
    "CourseCreateAPIView",
    "CourseListAPIView",
    "CourseRetrieveAPIView",
    "CourseUpdateAPIView",
    "CourseDeleteAPIView",
]