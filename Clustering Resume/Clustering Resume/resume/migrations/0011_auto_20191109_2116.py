# Generated by Django 2.2.6 on 2019-11-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_auto_20191109_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbti',
            name='author',
            field=models.CharField(max_length=20, verbose_name='작성자'),
        ),
    ]
