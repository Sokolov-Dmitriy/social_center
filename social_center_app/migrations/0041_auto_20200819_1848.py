# Generated by Django 3.0.8 on 2020-08-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_center_app', '0040_auto_20200818_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interpretationboyko',
            name='leisure',
            field=models.IntegerField(blank=True, choices=[(0, 'проблемы не выявлены'), (1, 'проблемы не выявлены'), (2, 'бедная сфера интересов'), (3, 'пассивный досуг ("убивает время")'), (4, 'отсутствие досуга, всё время посвящено употреблению')], null=True, verbose_name='Сфера досуга'),
        ),
    ]
