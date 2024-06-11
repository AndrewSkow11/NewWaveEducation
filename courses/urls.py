from django.urls import path
from courses import views

urlpatterns = [
    path('api/courses/', views.SeactionListCreate.as_view(), name='api_courses_list_create'),
    
]