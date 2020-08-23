# Generated by Django 3.0.8 on 2020-07-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_center_app', '0013_auto_20200730_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='husbandinformation',
            name='disabilityGroup',
            field=models.IntegerField(blank=True, choices=[(1, 'I группа'), (2, 'II группа'), (3, 'III группа')], null=True, verbose_name='Группа инвалидности'),
        ),
        migrations.AlterField(
            model_name='husbandinformation',
            name='specialSocialStatus',
            field=models.IntegerField(blank=True, choices=[(1, 'инвалидность'), (2, 'многодетная семья'), (3, 'одинокая мать'), (4, 'лицо из числа детей сирот и детей, оставшихся без попечения родителей')], null=True, verbose_name='Особый социальный статус'),
        ),
    ]
