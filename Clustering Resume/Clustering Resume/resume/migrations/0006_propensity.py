# Generated by Django 2.2.1 on 2019-10-07 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20191004_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propensity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.FloatField(default=0, verbose_name='적극적')),
                ('score2', models.FloatField(default=0, verbose_name='열정적')),
                ('score3', models.FloatField(default=0, verbose_name='성실성')),
                ('score4', models.FloatField(default=0, verbose_name='책임감')),
                ('score5', models.FloatField(default=0, verbose_name='사교적')),
                ('score6', models.FloatField(default=0, verbose_name='신중함')),
            ],
        ),
    ]
