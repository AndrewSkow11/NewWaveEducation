from django.urls import path
from . import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register("api/answer", views.AnswerAPIViewSet)
router.register("api/question", views.QuestionAPIViewSet)
router.register("api/quiz", views.QuizAPIViewSet)

# для интерактивного представления
urlpatterns = [
    path("", views.start_quiz_view, name="start"),
    path(
        "get-questions/start",
        views.get_questions,
        {"is_start": True},
        name="get-questions",
    ),
    path(
        "get-questions",
        views.get_questions,
        {"is_start": False},
        name="get-questions",
    ),
    path("get-answer", views.get_answer, name="get-answer"),
    path("get-finish", views.get_finish, name="get-finish"),
]
# для rest api
urlpatterns += router.urls
