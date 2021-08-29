from django.contrib import admin

# Register your models here.
from .models import Category, Student, Question, Questions_Answer, Karnameh

admin.site.register(Category)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Questions_Answer)
admin.site.register(Karnameh)