from django.urls import path
from courses import views

urlpatterns = [
    path(
        'api/courses/materials/list/',
        views.MaterialListAPIView.as_view(),
        name='material_list'
    ),
    path(
        'api/courses/<int:pk>/material/',
        views.MaterialRetrieveAPIView.as_view(),
        name='material_retrieve'
    ),
    path(
        'api/courses/sections/list/',
        views.SectionListAPIView.as_view(),
        name='section_list'
    ),
    path(
        'api/courses/<int:pk>/section/',
        views.SectionRetrieveAPIView.as_view(),
        name='section_retrieve'
    ),

]
