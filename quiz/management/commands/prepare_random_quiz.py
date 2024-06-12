from django.core.management.base import BaseCommand, CommandError

from quiz.models import Category, Question, Quiz


class Command(BaseCommand):
    help = 'Creates random quizes based on available categorys'

    def handle(self, *args, **options):
        if not Category.objects.count():
            raise CommandError('No categorys are available')
        Quiz.objects.all().delete()
        for category in Category.objects.all():
            quiz = Quiz(quiz_title='{} quiz'.format(category.title),
                        category=category)
            quiz.save()
            questions = list(Question.objects.filter(category=category))
            quiz.question.add(*questions)
            quiz.save()
        self.stdout.write(self.style.SUCCESS('Quiz Created'))