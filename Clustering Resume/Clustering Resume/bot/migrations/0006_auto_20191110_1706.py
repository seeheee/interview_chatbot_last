# Generated by Django 2.2.6 on 2019-11-10 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_questionlist_my_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionlist',
            name='my_resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pk', to='resume.Resume'),
        ),
    ]