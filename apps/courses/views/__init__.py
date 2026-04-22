from .category import (
    CategoryCreateAPIView,
    CategoryDeleteAPIView,
    CategoryListAPIView,
    CategoryRetrieveAPIView,
    CategoryUpdateAPIView,
)
from .course import (
    CourseListAPIView,
    CourseRetrieveAPIView,
)
from .tag import (
    TagCreateAPIView,
    TagDeleteAPIView,
    TagListAPIView,
    TagRetrieveAPIView,
    TagUpdateAPIView,
)


from .enrollment import (
    EnrollmentCreateAPIView,
    EnrollmentDeleteAPIView,
    EnrollmentListAPIView,
    EnrollmentRetrieveAPIView,
    EnrollmentUpdateAPIView,
)


__all__ = [
    "CategoryListAPIView",
    "CategoryCreateAPIView",
    "CategoryUpdateAPIView",
    "CategoryRetrieveAPIView",
    "CategoryDeleteAPIView",

    "TagListAPIView",
    "TagCreateAPIView",
    "TagUpdateAPIView",
    "TagRetrieveAPIView",
    "TagDeleteAPIView",

    "CourseListAPIView",
    "CourseRetrieveAPIView",

    "EnrollmentCreateAPIView",
    "EnrollmentDeleteAPIView",
    "EnrollmentListAPIView",
    "EnrollmentRetrieveAPIView",
    "EnrollmentUpdateAPIView",
]
