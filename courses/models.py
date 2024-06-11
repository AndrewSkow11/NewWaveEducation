from django.db import models

# Create your models here.
class Section(models.Model):
    """Модель описывает разделы учебных матриалов"""
    title = models.CharField(max_length=255, verbose_name='заголовок')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'

    def __str__(self):
        return self.title
    