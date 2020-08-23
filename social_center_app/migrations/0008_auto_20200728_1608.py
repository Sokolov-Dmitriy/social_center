# Generated by Django 3.0.8 on 2020-07-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_center_app', '0007_auto_20200725_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asocialbehavior',
            name='durationOfRemissionA',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Длительность ремиссии (в годах)(алкоголь)'),
        ),
        migrations.AlterField(
            model_name='asocialbehavior',
            name='durationOfRemissionD',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Длительность ремиссии (в годах)(наркотики)'),
        ),
        migrations.AlterField(
            model_name='asocialbehavior',
            name='durationOfUse',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Длительность употрбления (в годах)'),
        ),
    ]
