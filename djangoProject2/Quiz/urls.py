
from django.urls import path

from .views import show_students, exam

urlpatterns = [
    path('students/', show_students),
    path('exam/<str:student_name>', exam),
]


