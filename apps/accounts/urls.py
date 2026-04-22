from django.urls import path

from apps.accounts.views import (
    AuthorCreateAPIView,
    AuthorDeleteAPIView,
    AuthorDetailAPIView,
    AuthorListAPIView,
    AuthorUpdateAPIView,
    EducationCreateAPIView,
    EducationDeleteAPIView,
    EducationDetailAPIView,
    EducationListAPIView,
    EducationUpdateAPIView,
    UserDisableAPIView,
    UserProfileAPIView,
    UserRegisterAPIView,
    UserRegisterConfirmAPIView,
    UserProfileUpdateAPIView,
)

urlpatterns = [
    path("accounts/register/", UserRegisterAPIView.as_view(), name="register"),
    path(
        "accounts/register/confirm/",
        UserRegisterConfirmAPIView.as_view(),
        name="register-confirm",
    ),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path("profile/update/", UserProfileUpdateAPIView.as_view(), name="profile-update"),
    path("profile/disable/", UserDisableAPIView.as_view(), name="profile-disable"),
    path("education/list", EducationListAPIView.as_view(), name="educations"),
    path("education/create", EducationCreateAPIView.as_view(), name="education-create"),
    path(
        "education/delete/<int:id>",
        EducationDeleteAPIView.as_view(),
        name="education-delete",
    ),
    path(
        "education/update/<int:id>",
        EducationUpdateAPIView.as_view(),
        name="education-update",
    ),
    path(
        "education/<int:id>", EducationDetailAPIView.as_view(), name="education-single"
    ),
    path("author/list", AuthorListAPIView.as_view(), name="authors"),
    path("author/create", AuthorCreateAPIView.as_view(), name="author-create"),
    path("author/delete/<int:id>", AuthorDeleteAPIView.as_view(), name="author-delete"),
    path("author/update/<int:id>", AuthorUpdateAPIView.as_view(), name="author-update"),
    path("author/<int:id>", AuthorDetailAPIView.as_view(), name="author-single"),
]
