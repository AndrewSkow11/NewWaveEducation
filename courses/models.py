from django.db import models

class Section(models.Model):
    """Модель описывает разделы учебных матриалов"""
    title = models.CharField(max_length=255, verbose_name='заголовок')
    description = models.TextField(
        verbose_name='описание',
        null=True,
        blank=True),
    
    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'

    def __str__(self):
        return self.title
    

class Material(models.Model):
    """Учебный материал в разделе позволяет добавлять
    текстовый контент, видео, файл"""
    section = models.ForeignKey(
        Section, 
        verbose_name='учебный материал',
        related_name='material',
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    text_content = models.TextField(
        verbose_name='текстовая часть материала',
        null=True,
        blank=True
    )
    file_content = models.FileField(
        verbose_name='файл материла',
        upload_to='file_marerial',
        null=True,
        blank=True,
    )
    video_url = models.URLField(
        verbose_name='ссылка на видео',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материлы'