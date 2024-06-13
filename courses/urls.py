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
    SectionDestroyAPIView
)

urlpatterns = [
    #  -----materials----------
    path("materials/", MaterialListAPIView.as_view(),
         name="materials_list"),
    path("materials/<int:pk>/", MaterialRetrieveAPIView.as_view(),
         name="materials_retrieve/"),
    path("materials/create/", MaterialCreateAPIView.as_view(),
         name="materials_create/"),
    path("materials/update/<int:pk>/", MaterialUpdateAPIView.as_view(),
         name="material_update/"),
    path("materials/destroy/<int:pk>/", MaterialDestroyAPIView.as_view(),
         name="material_destroy"),
    #  -----sections----------
    path("sections/", SectionListAPIView.as_view(),
         name="sections_list"),
    path("sections/<int:pk>/", SectionRetrieveAPIView.as_view(),
         name="sections_retrieve"),
    path("sections/create/", SectionCreateAPIView.as_view(),
         name="sections_create"),
    path("sections/update/<int:pk>/", SectionUpdateAPIView.as_view(),
         name="sections_update"),
    path("sections/destroy/<int:pk>/", SectionDestroyAPIView.as_view(),
         name="sections_destroy"),

]
