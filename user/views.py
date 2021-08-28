import json
import re

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as _login
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse
from django.db import IntegrityError

from category_question.models import Questions, Answer

User = get_user_model()


# should  be add at utils
def password_checker():
    password = input("Enter string to test: ")
    if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return password
    else:
        return "not valid"


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        info = json.loads(request.body)
        try:
            if password_checker() == "password":
                user_dict = User.objects.create_studdent(info['username'], info['email'], info['password'])
                return HttpResponse(user_dict)
                # return JsonResponse(user_dict)
        except IntegrityError:
            return HttpResponse('should be unique')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        info = json.loads(request.body)
        user = authenticate(username=info['username'], password=info['password'])
        if user:
            _login(request, user)
            return HttpResponse("OK!")
        else:
            return HttpResponse("bad sensitive input !!")


@csrf_exempt
def who(request):
    return HttpResponse([request.user])


@csrf_exempt
def answer_question(request):
    data = json.loads(request.body)
    for answer in data['answers']:
        question_obj = Questions.objects.get(title=answer['title'])
        Answer.objects.create(user=request.user,
                              question=question_obj,
                              answer=answer['answer'])
