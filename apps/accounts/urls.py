from django.urls import path

from apps.accounts.apis.views import (
    AuthorListCreateAPIView,
    AuthorRetrieveUpdateDestroyAPIView,
    CountryListCreateAPIView,
    CountryRetrieveUpdateDestroyAPIView,
    RegionListCreateAPIView,
    RegionRetrieveUpdateDestroyAPIView,
    UserProfileAPIView,
    UserRegisterAPIView,
)

urlpatterns = [
    path("accounts/register/", UserRegisterAPIView.as_view(), name="register"),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path(
        "author/listcreate", AuthorListCreateAPIView.as_view(), name="author-listcreate"
    ),
    path(
        "author/retriveupdatedestroy",
        AuthorRetrieveUpdateDestroyAPIView.as_view(),
        name="author-retrieveupdatedestroy",
    ),
    path(
        "country/listcreate", CountryListCreateAPIView.as_view(), name="country-listcreate"
    ),
    path(
        "country/retrieveupdatedestroy",
        CountryRetrieveUpdateDestroyAPIView.as_view(),
        name="country-retrieveupdatedestroy",
    ),
    path(
        "region/listcreate", RegionListCreateAPIView.as_view(), name="region-listcreate"
    ),
    path(
        "region/retrieveupdatedestroy",
        RegionRetrieveUpdateDestroyAPIView.as_view(),
        name="region-retrieveupdatedestroy",
    ),
]
