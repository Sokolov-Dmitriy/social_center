# Generated by Django 3.0.8 on 2020-08-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_center_app', '0002_auto_20200824_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsocrates',
            name='attempt',
            field=models.IntegerField(choices=[(1, 'Первичная'), (2, 'Вторичная')], verbose_name='Диагностика'),
        ),
    ]
