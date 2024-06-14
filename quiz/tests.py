from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Quiz, Question, Answer


class AnswerAPITest(APITestCase):

    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword",
            is_superuser=True,
        )
        self.quiz = Quiz.objects.create(
            name="Test Quiz", owner=self.admin_user
        )
        self.question = Question.objects.create(
            quiz=self.quiz, text="Test Question", owner=self.admin_user
        )
        self.answer = Answer.objects.create(
            question=self.question,
            text="something answer",
            is_correct=True,
            owner=self.admin_user,
        )

    def test_create_answer(self):
        url = reverse("answer-list")
        data = {"text": "Test Answer", "question": self.question.pk}
        self.client.force_login(self.admin_user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_answers(self):
        url = reverse(
            "answer-detail",
            args=[
                self.answer.pk,
            ],
        )
        self.client.force_login(self.admin_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class QuestionAPITest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword",
            is_superuser=True,
        )
        self.quiz = Quiz.objects.create(
            name="Test Quiz", owner=self.admin_user
        )
        self.question = Question.objects.create(
            quiz=self.quiz, text="Test Question", owner=self.admin_user
        )
        self.answer = Answer.objects.create(
            question=self.question,
            text="something answer",
            is_correct=True,
            owner=self.admin_user,
        )

    def test_create_question(self):
        url = reverse("question-list")
        data = {"text": "Test Question", "quiz": self.quiz.pk}
        self.client.force_login(self.admin_user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_questions(self):
        url = reverse("question-list")
        self.client.force_login(self.admin_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class QuizAPITest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword",
            is_superuser=True,
        )
        self.quiz = Quiz.objects.create(
            name="Test Quiz", owner=self.admin_user
        )
        self.question = Question.objects.create(
            quiz=self.quiz, text="Test Question", owner=self.admin_user
        )
        self.answer = Answer.objects.create(
            question=self.question,
            text="something answer",
            is_correct=True,
            owner=self.admin_user,
        )

    def test_create_quiz(self):
        url = reverse("quiz-list")
        data = {"name": "Test Quiz"}
        self.client.force_login(self.admin_user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_quizzes(self):
        url = reverse("quiz-list")
        self.client.force_login(self.admin_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
