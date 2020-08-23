# Generated by Django 3.0.8 on 2020-08-03 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_center_app', '0017_auto_20200803_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interpretationboyko',
            name='work_activity',
            field=models.IntegerField(choices=[(2, 'выраженные проблемы на работе, но не приводящие к её потере'), (3, 'серьёзные проблемы при работе, не позволяющие её сохранить'), (4, 'нет работы, не способен её самостоятельно найти и выполнять')], verbose_name='Трудовая (профессиональная) деятельность'),
        ),
    ]
