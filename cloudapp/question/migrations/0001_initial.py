# Generated by Django 2.2.5 on 2021-02-12 07:30

from django.db import migrations, models
import django.db.models.deletion
import question.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.CharField(db_column='id', max_length=20, primary_key=True, serialize=False)),
                ('context', models.CharField(db_column='CONTEXT', default='', max_length=1000)),
                ('choice1', models.CharField(db_column='CHOICE1', default='', max_length=400)),
                ('choice2', models.CharField(db_column='CHOICE2', default='', max_length=400)),
                ('choice3', models.CharField(db_column='CHOICE3', default='', max_length=400)),
                ('choice4', models.CharField(db_column='CHOICE4', default='', max_length=400)),
                ('correct', models.IntegerField(db_column='CORRECT', default=1, validators=[question.models.validate_choice])),
                ('exam_id', models.ForeignKey(db_column='EXAMID', default=None, on_delete=django.db.models.deletion.CASCADE, to='exam.Exam')),
            ],
            options={
                'db_table': 'QUESTION',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.CharField(db_column='id', max_length=20, primary_key=True, serialize=False)),
                ('answer', models.IntegerField(db_column='ANSWER', default=1, validators=[question.models.validate_choice])),
                ('assingment_id', models.ForeignKey(db_column='ASNID', default='', on_delete=django.db.models.deletion.CASCADE, to='exam.Assignment')),
                ('question_id', models.ForeignKey(db_column='QUESTID', default='', on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
            ],
            options={
                'db_table': 'ANSWER',
                'unique_together': {('question_id', 'assingment_id')},
            },
        ),
    ]
