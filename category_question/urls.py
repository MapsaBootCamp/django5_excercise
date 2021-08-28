from django.urls import path
from .views import exam_answer, exam_maker

urlpatterns = [
    path("exam_maker/", exam_maker, name='start'),
    path("exam_answer/", exam_answer, name='answer')
]
