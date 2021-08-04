# Generated by Django 3.2.5 on 2021-08-02 15:12

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20210802_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsanswers',
            name='correct_percentage',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='درصد صحیح جواب'),
        ),
        migrations.AlterField(
            model_name='studentsanswers',
            name='answer_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), blank=True, null=True, size=None, verbose_name='شماره جواب'),
        ),
        migrations.AlterField(
            model_name='studentsanswers',
            name='questions_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None, verbose_name='شماره سوال'),
        ),
        migrations.AlterField(
            model_name='studentsanswers',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.students', verbose_name='نام دانش آموز'),
        ),
    ]
