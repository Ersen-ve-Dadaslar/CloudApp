# Generated by Django 2.2.5 on 2021-02-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20210212_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='completed',
            field=models.BooleanField(db_column='COMPLETED', default=False),
        ),
    ]
