# Generated by Django 4.1 on 2022-11-19 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadoraAdjudicacion', '0004_alter_valoractualizado_cod_hzte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valoractualizado',
            name='fecha_valor',
            field=models.DateField(default=datetime.date(2022, 11, 19)),
        ),
    ]
