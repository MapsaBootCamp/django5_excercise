from django.contrib.postgres.fields import ArrayField
from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام دانش آموز", unique=True)

    class Meta:
        verbose_name = "دانش آموز"
        verbose_name_plural = "دانش آموزان"

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته بندی")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name


class Questions(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان سوال")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوالات"

    def __str__(self):
        return self.title


class QuestionsAnswers(models.Model):
    option = models.CharField(max_length=300, verbose_name="گزینه")
    is_correct = models.BooleanField(default=False, verbose_name="گزینه صحیح")
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='qanswer')

    class Meta:
        verbose_name = "جواب سوالات"
        verbose_name_plural = " جواب های سوالات"

    def __str__(self):
        return self.option


class StudentsAnswers(models.Model):
    questions_id = ArrayField(ArrayField(models.IntegerField()), verbose_name="شماره سوال")
    answer_id = ArrayField(ArrayField(models.IntegerField()), verbose_name="شماره جواب", blank=True, null=True)
    correct_percentage = models.IntegerField(blank=True, null=True, default=0, verbose_name="درصد صحیح جواب")
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="نام دانش آموز")

    class Meta:
        verbose_name = "جواب دانش آموز"
        verbose_name_plural = "جواب های دانش آموزان"
