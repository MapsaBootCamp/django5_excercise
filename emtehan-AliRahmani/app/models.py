from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    discription = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "CATEGORY"
        verbose_name_plural = "گروه بندی ها"

    def __str__(self):
        return self.title


class Questios(models.Model):
    body = models.TextField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Answers(models.Model):
    body = models.TextField()
    true_or_false = models.BooleanField(default=False)
    question = models.ForeignKey(Questios, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Students(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score = models.FloatField(blank=True, null=True)
    resume = None

    def __str__(self):
        return self.name


class studentAnswers(models.Model):
    questions_id = ArrayField(ArrayField(models.IntegerField()), verbose_name="شماره سوال")
    answer_id = ArrayField(ArrayField(models.IntegerField()), verbose_name="شماره جواب", blank=True, null=True)
    correct_percentage = models.FloatField(blank=True, null=True, default=0, verbose_name="درصد صحیح جواب")
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="نام دانش آموز")

    def __str__(self):
        return self.name
