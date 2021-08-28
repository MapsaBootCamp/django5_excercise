import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Questions, Answer, Exam, Categories

METHOD_GET = "GET"


@require_http_methods(["GET"])
@csrf_exempt
def exam_maker(request, user):
    if user.objects.filter(name=user).count() <= 0:
        return JsonResponse(f"{user} dose not exists", safe=False)
    if request.method == METHOD_GET:
        developer = Questions.objects.filter(category_id=1).order_by('?').values('id', 'title')[:1]
        DBA = Questions.objects.filter(category_id=2).order_by('?').values('id', 'title')[:1]
        devops = Questions.objects.filter(category_id=3).order_by('?').values('id', 'title')[:1]
        sys_admin = Questions.objects.filter(category_id=4).order_by('?').values('id', 'title')[:1]

        # -------->for selecting question in category we should use prefetch_related
        questions = []
        # questions = {"developer":first_cat, "developer"":second_cat, "devops":third_cat,"sys_admin": fourth_cat}

        for i in range(1, 21):
            if i < 6:
                questions.append(developer)
            elif 5 < i & i < 11:
                questions.append(DBA)
            elif 11 <= i & i <= 15:
                questions.append(devops)
            else:
                questions.append(sys_admin)

        # questions_obj = Questions.objects.filter(questions)
        questions_id = [qid['id'] for qid in questions]
        exam_obj = Exam.objects.create(request.user)

        for qid in questions_id:
            exam_obj.questions.add(qid)
        exam_obj.save()
        return JsonResponse({"id": exam_obj.id, "questions": questions_id})


@csrf_exempt
def exam_answer(request):
    if request.method == "POST":
        result = 0
        info = json.loads(request.body)
        exam_obj = get_object_or_404(Exam, id=info["id"])
        if exam_obj.result is not None:
            return JsonResponse({"this exam has been completed"})
        for question in info['questions']:
            ques_obj = get_object_or_404(Questions, title=Questions(['title']))
            exam_obj.answers.add(Answer.objects.create(user=request.user, question=ques_obj, answer=question['answer']))

            if int(question['answer']) == ques_obj.correct_choice:
                result += 1
            else:
                result -= 0.33

        result = (result / 20) * 100
        exam_obj.result = result
        exam_obj.save()
        return JsonResponse({"result": result})
