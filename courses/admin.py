from django.contrib import admin

from quiz.models import (
    Answer,
    Category,
    Question,
    Quiz
)

# Register your models here.
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Quiz)