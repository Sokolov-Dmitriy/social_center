# Generated by Django 3.0.8 on 2020-08-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_center_app', '0043_auto_20200821_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chronicdisease',
            name='HIVStatus',
            field=models.IntegerField(blank=True, choices=[(1, 'есть'), (2, 'нет')], null=True, verbose_name='ВИЧ-статус'),
        ),
        migrations.AlterField(
            model_name='chronicdisease',
            name='hepatitisC',
            field=models.IntegerField(blank=True, choices=[(1, 'есть'), (2, 'нет')], null=True, verbose_name='Гепатит С'),
        ),
    ]
