# Generated by Django 3.0.8 on 2020-07-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_center_app', '0004_auto_20200720_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='number_children',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество детей'),
        ),
    ]
