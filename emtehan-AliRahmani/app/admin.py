from django.contrib import admin

from .models import Category, Questios, Answers, Students, studentAnswers


# Register your models here.

class AnsAdmin(admin.ModelAdmin):
    list_display = ["question_id","true_or_false"]
    list_filter = ["question_id"]
admin.site.register(Answers,AnsAdmin)


class CatAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CatAdmin)


class StuAnsAdmin(admin.ModelAdmin):
    pass
admin.site.register(studentAnswers, StuAnsAdmin)


@admin.register(Students)
class StuAdmin(admin.ModelAdmin):
    list_filter = [ "id"]


# class AnswerInLine(admin.StackedInline):
#     """
#     در دیتابیس sqlite نمیتوان این کار را انجام داد ارور database LOCKED را بر میگرداند
#     """
#     model = Answers
#     extra = 4

@admin.register(Questios)
class QusetionsAdmin(admin.ModelAdmin):
    # inlines = [AnswerInLine]
    list_display = ['__str__', "id", ]
    list_filter = [ "cat"]