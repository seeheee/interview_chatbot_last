# Generated by Django 2.2.6 on 2019-11-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_mbti_my_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='MBTI_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='작성자')),
                ('E_s', models.FloatField(default=0, verbose_name='E_s')),
                ('I_s', models.FloatField(default=0, verbose_name='I_s')),
                ('N_s', models.FloatField(default=0, verbose_name='N_s')),
                ('S_s', models.FloatField(default=0, verbose_name='S_s')),
                ('T_s', models.FloatField(default=0, verbose_name='T_s')),
                ('F_s', models.FloatField(default=0, verbose_name='F_s')),
                ('J_s', models.FloatField(default=0, verbose_name='J_s')),
                ('P_s', models.FloatField(default=0, verbose_name='P_s')),
                ('result', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
