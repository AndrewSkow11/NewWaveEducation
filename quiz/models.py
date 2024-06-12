from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='загаловок'
    )

    class Meta:
        verbose_name = 'категория '
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer_text = models.CharField(
        max_length=255,
        verbose_name='текст ответа'
    )

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'текст ответа'
        verbose_name_plural = 'тексты ответов'


class Question(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name='категория'
    )
    question_text = models.CharField(
        max_length=255,
        verbose_name='текст вопроса'
    )
    answer = models.OneToOneField(
        'Answer',
        on_delete=models.CASCADE,
        related_name='correct_answer',
        null=True,
        blank=True,
        verbose_name='правильный ответ'
    )
    choices = models.ManyToManyField(
        Answer,
        related_name='choices',
        verbose_name='выбор ответа'
    )

    def __str__(self):
        return self.question_text


class Quiz(models.Model):
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    quiz_title = models.CharField(
        max_length=255,
        verbose_name='заголовок теста'
    )
    question = models.ManyToManyField(
        Question,
        blank=True,
        verbose_name='вопрос'
    )

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    def __str__(self):
        return self.quiz_title
