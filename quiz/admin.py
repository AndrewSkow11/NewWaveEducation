from django.contrib import admin
from quiz.models import Quiz, Question, Answer

admin.site.register(Quiz)
admin.site.register(Answer)


class QuestionInlineModel(admin.TabularInline):
    model = Question
    fields = [
        "quiz" "text",
    ]


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ["question", "text", "is_correct"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ["quiz", "text"]
    inlines = [AnswerInlineModel]
