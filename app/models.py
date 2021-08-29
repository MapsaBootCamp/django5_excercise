from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here


class Category(models.Model):
     name = models.CharField(max_length=200)

     def __str__(self):
         return self.name


class Question(models.Model):
    questions = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name="عنوان سوال", null=True)

    def __str__(self):
        return self.questions


class Questions_Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    true_or_false = models.BooleanField(blank=True, null=True)
    options = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.question} - {self.true_or_false} - {self.options}"


class Student(models.Model):
    student_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.student_name


class Karnameh(models.Model):
    question_id = ArrayField(ArrayField(models.IntegerField()), verbose_name="شماره سوال")
    answer_id = ArrayField(ArrayField(models.IntegerField()),verbose_name="شماره جواب", blank=True, null=True)
    correct_percentage = models.IntegerField(blank=True, null=True, default=0, verbose_name="درصد جواب صحیح")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="نام دانش آموز")

    def __str__(self):
        return f"{self.question_id} - {self.answer_id} - {self.correct_percentage} - {self.student }"




