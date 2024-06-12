from django.db import models


class Quiz(models.Model):
    name = models.CharField(
        verbose_name='Название теста',
        max_length=300)

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name='название теста'
    )
    text = models.CharField(
        max_length=300,
        verbose_name='текст вопроса'
    )

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='вопрос')
    text = models.CharField(
        max_length=300,
        verbose_name='текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='правильность ответа')

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'

    def __str__(self):
        return f'{self.text} {self.is_correct}'
