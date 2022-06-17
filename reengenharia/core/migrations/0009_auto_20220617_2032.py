# Generated by Django 3.2.13 on 2022-06-17 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220617_2008'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agendamento',
        ),
        migrations.AddField(
            model_name='atividade',
            name='equipamentos',
            field=models.ManyToManyField(to='core.Equipamento'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='dia_semana',
            field=models.CharField(max_length=255),
        ),
    ]
