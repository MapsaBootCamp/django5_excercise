from django.contrib import admin

from .models import Students, Questions, QuestionsAnswers, StudentsAnswers, Categories


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # if OnlineQuiz.settings.LANGUAGE_CODE==
    pass


class AnswerInLine(admin.StackedInline):
    model = QuestionsAnswers
    extra = 4


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine, ]
    list_display = ['__str__', 'category']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentsAnswers)
class StudentsAnswersAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Students)
# admin.site.register(StudentsAnswers)
# admin.site.register(Questions)
# admin.site.register(Categories)
# admin.site.register(QuestionsAnswers)
