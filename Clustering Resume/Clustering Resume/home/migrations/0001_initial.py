# Generated by Django 2.2.5 on 2019-09-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Introduces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motive', models.CharField(max_length=200)),
                ('dream', models.CharField(max_length=200)),
                ('growth', models.CharField(max_length=200)),
                ('PAC', models.CharField(max_length=200)),
                ('activities', models.CharField(max_length=200)),
            ],
        ),
    ]
