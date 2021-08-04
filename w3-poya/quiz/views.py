import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Students, Questions, QuestionsAnswers, StudentsAnswers


def show_students(request):
    all_students = list(Students.objects.all().values()) or "هیچ دانش آموزی موجود نیست"
    return JsonResponse(all_students, safe=False)


@csrf_exempt
def exam(request, student_name):
    if Students.objects.filter(name=student_name).count() <= 0:
        return JsonResponse(f"{student_name} dose not exists", safe=False)
    # check if user exist
    if request.method == "GET":
        cat = []
        cat1 = Questions.objects.filter(category_id=3).order_by('?').values('id', 'title')[:1]
        cat2 = Questions.objects.filter(category_id=4).order_by('?').values('id', 'title')[:1]
        cat3 = Questions.objects.filter(category_id=5).order_by('?').values('id', 'title')[:1]
        cat4 = Questions.objects.filter(category_id=6).order_by('?').values('id', 'title')[:1]
        # get random questions from each categories
        cat = [qs for qs in cat1]
        cat += [qs for qs in cat2]
        cat += [qs for qs in cat3]
        cat += [qs for qs in cat4]
        # concatenate all categories to one
        questions_id = [qid['id'] for qid in cat]
        # get all chosen questions id
        if Students.objects.get(name=student_name):
            StudentsAnswers.objects.create(questions_id=questions_id, answer_id=[],
                                           student=Students.objects.get(name=student_name))
        # save questions id into students answer model
        for question in cat:
            question['answers'] = list(
                QuestionsAnswers.objects.filter(question_id=question['id']).values('id', 'option'))
        # get options of each questions from questions answer model
        return JsonResponse(list(cat), safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        question_id = [answer['question_id'] for answer in data]
        answer_id = [int(answer['answer_id']) for answer in data]
        # get users data from post method
        correct_answer = []
        for qid in question_id:
            correct_answer += list(QuestionsAnswers.objects.filter(question_id=qid, is_correct=True).values('id'))
        # get id of correct answers of asked questions
        correct_counter = 0
        for aid in correct_answer:
            if aid['id'] in answer_id:
                correct_counter += 1
        # compare user answers to correct answers of asked questions and count the corrects
        correct_percentage = (correct_counter / len(correct_answer)) * 100
        StudentsAnswers.objects.filter(questions_id=question_id, student__name=student_name).update(answer_id=answer_id,
                                                                                                    correct_percentage=correct_percentage)
        # add users answer to database of asked questions
        # calculate percentage of correct answers
        return JsonResponse(correct_percentage, safe=False)
