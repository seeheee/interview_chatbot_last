# Generated by Django 2.2.6 on 2019-11-10 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20191110_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='my_resume',
            field=models.IntegerField(default=0),
        ),
    ]
