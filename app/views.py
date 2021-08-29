from django.shortcuts import render

# Create your views here
from .models import Student, Category, Questions_Answer, Question, Karnameh
import json
from django.http import HttpResponse, JsonResponse


def show_questions(request):
    qs = Question.objects.all().values()
    return JsonResponse(qs,safe=True)


def show_answers(request):
    qs = Questions_Answer.objects.all().values()
    return JsonResponse(qs, safe=True)
