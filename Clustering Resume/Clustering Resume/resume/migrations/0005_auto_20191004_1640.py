# Generated by Django 2.2.1 on 2019-10-04 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20190916_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='author',
            field=models.CharField(max_length=16, verbose_name='작성자'),
        ),
    ]
