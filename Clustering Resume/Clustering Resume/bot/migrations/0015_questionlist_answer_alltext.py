# Generated by Django 2.2.5 on 2019-11-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0014_auto_20191129_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionlist',
            name='answer_alltext',
            field=models.TextField(default='', verbose_name='전체답변'),
        ),
    ]
