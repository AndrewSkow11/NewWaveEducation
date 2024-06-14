from django.urls import path
from courses.views import (
    MaterialListAPIView,
    MaterialRetrieveAPIView,
    MaterialCreateAPIView,
    MaterialUpdateAPIView,
    MaterialDestroyAPIView,
    SectionListAPIView,
    SectionRetrieveAPIView,
    SectionCreateAPIView,
    SectionUpdateAPIView,
    SectionDestroyAPIView,
)

urlpatterns = [
    #  -----materials----------
    path(
        "api/materials/", MaterialListAPIView.as_view(), name="materials_list"
    ),
    path(
        "api/materials/<int:pk>/",
        MaterialRetrieveAPIView.as_view(),
        name="materials_retrieve",
    ),
    path(
        "api/materials/create/",
        MaterialCreateAPIView.as_view(),
        name="materials_create",
    ),
    path(
        "api/materials/update/<int:pk>/",
        MaterialUpdateAPIView.as_view(),
        name="material_update",
    ),
    path(
        "api/materials/destroy/<int:pk>/",
        MaterialDestroyAPIView.as_view(),
        name="material_destroy",
    ),
    #  -----sections----------
    path("api/sections/", SectionListAPIView.as_view(), name="sections_list"),
    path(
        "api/sections/<int:pk>/",
        SectionRetrieveAPIView.as_view(),
        name="sections_retrieve",
    ),
    path(
        "api/sections/create/",
        SectionCreateAPIView.as_view(),
        name="sections_create",
    ),
    path(
        "api/sections/update/<int:pk>/",
        SectionUpdateAPIView.as_view(),
        name="sections_update",
    ),
    path(
        "api/sections/destroy/<int:pk>/",
        SectionDestroyAPIView.as_view(),
        name="sections_destroy",
    ),
]
