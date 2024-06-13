from django.urls import path
from . import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register("answer", views.AnswerAPIViewSet)
router.register("question", views.QuestionAPIViewSet)
router.register("quiz", views.QuizAPIViewSet)

urlpatterns = [
                  path('', views.start_quiz_view, name='start'),
                  path('get-questions/start', views.get_questions, {'is_start': True}, name='get-questions'),
                  path('get-questions', views.get_questions, {'is_start': False}, name='get-questions'),
                  path('get-answer', views.get_answer, name='get-answer'),
                  path('get-finish', views.get_finish, name='get-finish'),
              ] + router.urls
