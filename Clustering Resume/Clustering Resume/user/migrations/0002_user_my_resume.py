# Generated by Django 2.2.5 on 2019-10-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='my_resume',
            field=models.CharField(choices=[('', ''), ('삼성전자', '삼성전자')], default=True, max_length=80),
        ),
    ]
