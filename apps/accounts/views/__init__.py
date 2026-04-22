from .auth import (
    UserDisableAPIView,
    UserProfileAPIView,
    UserRegisterAPIView,
    UserRegisterConfirmAPIView,
)
from .author_crud import (
    AuthorCreateAPIView,
    AuthorDeleteAPIView,
    AuthorDetailAPIView,
    AuthorListAPIView,
    AuthorUpdateAPIView,
)
from .education_crud import (
    EducationCreateAPIView,
    EducationDeleteAPIView,
    EducationDetailAPIView,
    EducationListAPIView,
    EducationUpdateAPIView,
)
from .auth import UserProfileUpdateAPIView

__all__ = [
    "UserRegisterAPIView",
    "UserRegisterConfirmAPIView",
    "UserProfileAPIView",
    "UserDisableAPIView",
    "AuthorCreateAPIView",
    "AuthorDeleteAPIView",
    "AuthorDetailAPIView",
    "AuthorListAPIView",
    "AuthorUpdateAPIView",
    "EducationCreateAPIView",
    "EducationDeleteAPIView",
    "EducationDetailAPIView",
    "EducationListAPIView",
    "EducationUpdateAPIView",
    "UserProfileUpdateAPIView",
]
