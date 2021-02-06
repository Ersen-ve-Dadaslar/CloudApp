# Generated by Django 2.2.5 on 2021-02-06 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'ASSIGNMENT',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.CharField(auto_created=True, db_column='EXAMID', max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='EXNAME', max_length=100)),
                ('start_time', models.DateTimeField(db_column='START')),
                ('end_time', models.DateTimeField(db_column='END')),
            ],
            options={
                'db_table': 'EXAM',
            },
        ),
    ]
