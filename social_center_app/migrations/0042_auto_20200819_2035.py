# Generated by Django 3.0.8 on 2020-08-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_center_app', '0041_auto_20200819_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interpretationboyko',
            name='friends',
            field=models.IntegerField(blank=True, choices=[(0, 'проблемы не выявлены'), (1, 'проблемы не выявлены'), (2, 'сужение контактов с людьми'), (3, 'суженый круг общения, часты конфликты c окружающими'), (4, 'отсутствие социальных связей')], null=True, verbose_name='Контакты с друзьями, знакомыми'),
        ),
    ]
