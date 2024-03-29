# Generated by Django 2.2.5 on 2019-10-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer1',
            field=models.TextField(default='', verbose_name='답변1'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer10',
            field=models.TextField(default='', verbose_name='답변10'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer11',
            field=models.TextField(default='', verbose_name='답변11'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer12',
            field=models.TextField(default='', verbose_name='답변12'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer13',
            field=models.TextField(default='', verbose_name='답변13'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer14',
            field=models.TextField(default='', verbose_name='답변14'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer15',
            field=models.TextField(default='', verbose_name='답변15'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer16',
            field=models.TextField(default='', verbose_name='답변16'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer2',
            field=models.TextField(default='', verbose_name='답변2'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer3',
            field=models.TextField(default='', verbose_name='답변3'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer4',
            field=models.TextField(default='', verbose_name='답변4'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer5',
            field=models.TextField(default='', verbose_name='답변5'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer6',
            field=models.TextField(default='', verbose_name='답변6'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer7',
            field=models.TextField(default='', verbose_name='답변7'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer8',
            field=models.TextField(default='', verbose_name='답변8'),
        ),
        migrations.AddField(
            model_name='questionlist',
            name='answer9',
            field=models.TextField(default='', verbose_name='답변9'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question1',
            field=models.TextField(default='', verbose_name='질문1'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question10',
            field=models.TextField(default='', verbose_name='질문10'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question11',
            field=models.TextField(default='', verbose_name='질문11'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question12',
            field=models.TextField(default='', verbose_name='질문12'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question13',
            field=models.TextField(default='', verbose_name='질문13'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question14',
            field=models.TextField(default='', verbose_name='질문14'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question15',
            field=models.TextField(default='', verbose_name='질문15'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question16',
            field=models.TextField(default='', verbose_name='질문16'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question2',
            field=models.TextField(default='', verbose_name='질문2'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question3',
            field=models.TextField(default='', verbose_name='질문3'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question4',
            field=models.TextField(default='', verbose_name='질문4'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question5',
            field=models.TextField(default='', verbose_name='질문5'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question6',
            field=models.TextField(default='', verbose_name='질문6'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question7',
            field=models.TextField(default='', verbose_name='질문7'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question8',
            field=models.TextField(default='', verbose_name='질문8'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='question9',
            field=models.TextField(default='', verbose_name='질문9'),
        ),
    ]
