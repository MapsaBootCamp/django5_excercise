import json
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Category, Questios, Answers, Students, studentAnswers


# Create your views here.

def show_all_students(request):
    stu = list(Students.objects.all().values_list())
    return JsonResponse(stu, safe=False)

def show_all_answers(request):
    ans = list(Answers.objects.all().values_list())
    return JsonResponse(ans, safe=False)


def show_all_questions(request):
    all_ask = list(Questios.objects.all().values())
    return JsonResponse(all_ask, safe=False)


@csrf_exempt
def exam(request, student_name):
    stu = Students.objects.count()
    if stu < 1 or (not (Students.objects.filter(name=student_name))):
        return JsonResponse(f"chizi nafrestadi ya kolan to system nisti")
    if request.method == "GET":
        # get random questions from each categories
        cat = list()
        cat1 = Questios.objects.filter(cat_id=1).order_by("?").values('id', 'body','cat__title')[:1]
        cat2 = Questios.objects.filter(cat_id=5).order_by("?").values('id', 'body','cat__title')[:1]
        cat3 = Questios.objects.filter(cat_id=6).order_by("?").values('id', 'body','cat__title')[:1]
        cat4 = Questios.objects.filter(cat_id=7).order_by("?").values('id', 'body','cat__title')[:1]

        # concatenate all categories to one
        cat = [qs for qs in cat1]
        cat += [qs for qs in cat2]
        cat += [qs for qs in cat3]
        cat += [qs for qs in cat4]

        # get all chosen questions id
        questions_id = [qid['id'] for qid in cat]

        ## save questions id into students answer model
        # if Students.objects.get(name=student_name):
        #     studentAnswers.objects.create(questions_id=questions_id,
        #                                   answer_id=[],
        #                                   student=Students.objects.get(name=student_name))

        # get options of each questions from questions answer model
        for question in cat:
            question['answers'] = list(
                Answers.objects.filter(id=question['id']).values('id', 'body'))

        return JsonResponse(list(cat), safe=False)


    # get users data from post method
    elif request.method == "POST":
        # get id of correct answers of asked questions
        data = json.loads(request.body)
        question_id = [answer['question_id'] for answer in data]
        answer_id = [int(answer['answer_id']) for answer in data]

        # compare user answers to correct answers of asked questions and count the corrects
        correct_answer = []
        for qid in question_id:
            correct_answer += list(Answers.objects.filter(question_id=qid, true_or_false=True).values('id'))

        # add users answer to database of asked questions
        correct_counter = 0
        for aid in correct_answer:
            if aid['id'] in answer_id:
                correct_counter += 1

        # calculate percentage of correct answers
        # correct_percentage = (correct_counter / len(correct_answer)) * 100
        if len(correct_answer) >= 0:
            correct_percentage = (correct_counter / len(correct_answer)) * 100
        else:
            correct_percentage = 0
        studentAnswers.objects.filter(questions_id=question_id,
                                      student__name=student_name).\
                                      update(answer_id=answer_id,
                                      correct_percentage=correct_percentage)

        return JsonResponse(correct_percentage, safe=False)
