# Generated by Django 2.2.5 on 2021-02-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20210207_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='result',
            field=models.IntegerField(db_column='RESULT', default=0),
        ),
    ]