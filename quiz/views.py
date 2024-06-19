from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db.models import Count
from .models import Quiz, Question, Answer
from typing import Optional
from django.contrib.auth.decorators import login_required

from quiz.serializers import (
    AnswerSerializer,
    QuizSerializer,
    QuestionSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from courses.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@login_required
def start_quiz_view(request) -> HttpResponse:
    topics = Quiz.objects.all().annotate(questions_count=Count("question"))
    return render(request, "start.html", context={"topics": topics})


@login_required
def get_questions(request, is_start=False) -> HttpResponse:
    if is_start:
        request = _reset_quiz(request)
        question = _get_first_question(request)
    else:
        question = _get_subsequent_question(request)
        if question is None:
            return get_finish(request)

    answers = Answer.objects.filter(question=question)
    request.session["question_id"] = (
        question.id
    )  # Update session state with current question id.

    return render(
        request,
        "partials/question.html",
        context={"question": question, "answers": answers},
    )


@login_required
def _get_first_question(request) -> Question:
    quiz_id = request.POST["quiz_id"]
    return Question.objects.filter(quiz_id=quiz_id).order_by("id").first()


@login_required
def _get_subsequent_question(request) -> Optional[Question]:
    quiz_id = request.POST["quiz_id"]
    previous_question_id = request.session["question_id"]

    try:
        return (
            Question.objects.filter(
                quiz_id=quiz_id, id__gt=previous_question_id
            )
            .order_by("id")
            .first()
        )
    except Question.DoesNotExist:  # I.e., there are no more questions.
        return None


@login_required
def get_answer(request) -> HttpResponse:
    submitted_answer_id = request.POST["answer_id"]
    submitted_answer = Answer.objects.get(id=submitted_answer_id)

    if submitted_answer.is_correct:
        correct_answer = submitted_answer
        request.session["score"] = request.session.get("score", 0) + 1
    else:
        correct_answer = Answer.objects.get(
            question_id=submitted_answer.question_id, is_correct=True
        )

    return render(
        request,
        "partials/answer.html",
        context={
            "submitted_answer": submitted_answer,
            "answer": correct_answer,
        },
    )


@login_required
def get_finish(request) -> HttpResponse:
    quiz = Question.objects.get(id=request.session["question_id"]).quiz
    questions_count = Question.objects.filter(quiz=quiz).count()
    score = request.session.get("score", 0)
    percent = int(score / questions_count * 100)
    request = _reset_quiz(request)

    return render(
        request,
        "partials/finish.html",
        context={
            "questions_count": questions_count,
            "score": score,
            "percent_score": percent,
        },
    )


@login_required
def _reset_quiz(request) -> HttpRequest:
    """
    We reset the quiz state to allow the user to start another quiz.
    """
    if "question_id" in request.session:
        del request.session["question_id"]
    if "score" in request.session:
        del request.session["score"]
    return request


# API

# Answer


class AnswerAPIViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAdminUser]
        elif self.action == "list":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "update":
            self.permission_classes = [IsOwner]
        elif self.action == "destroy":
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


# Question
class QuestionAPIViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAdminUser]
        elif self.action == "list":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "update":
            self.permission_classes = [IsOwner]
        elif self.action == "destroy":
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


# Quiz
class QuizAPIViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAdminUser]
        elif self.action == "list":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "update":
            self.permission_classes = [IsOwner]
        elif self.action == "destroy":
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()
