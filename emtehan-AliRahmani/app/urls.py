from django.urls import path

from .views import show_all_students, show_all_questions, exam,show_all_answers

urlpatterns = [
    path('show-all-students/', show_all_students),
    path('show-all-questions/', show_all_questions),
    path('show_all_answers/', show_all_answers),
    path('exam/<str:student_name>', exam),
]
