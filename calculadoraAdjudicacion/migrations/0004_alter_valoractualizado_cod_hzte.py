# Generated by Django 4.1 on 2022-11-15 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculadoraAdjudicacion', '0003_alter_planporadjudicar_vivienda_adjudicar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valoractualizado',
            name='cod_hzte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='calculadoraAdjudicacion.vivienda', to_field='cod_hzte'),
        ),
    ]
