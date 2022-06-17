# Generated by Django 3.2.13 on 2022-06-17 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220612_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='como_ficou_sabendo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='plano_saude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='por_que_academia',
            field=models.CharField(blank=True, choices=[['APRENDER_A_NADAR', 'APRENDER A NADAR'], ['BRONQUITE', 'APRENDER A NADAR'], ['COLUNA', 'APRENDER A NADAR'], ['OBESIDADE', 'APRENDER A NADAR'], ['TREINAR', 'APRENDER A NADAR'], ['MANTER_A_FORMA', 'APRENDER A NADAR'], ['APRENDER_A_NADAR', 'APRENDER A NADAR']], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='pratica_outro_esporte',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='ProdutoVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.venda')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_exame', models.DateField()),
                ('validade_exame', models.DateField()),
                ('inicio_contrato', models.DateField()),
                ('vencimento_contrato', models.DateField()),
                ('valor_pre_contrato', models.FloatField()),
                ('pagamento_pre_contrato', models.FloatField()),
                ('desconto_matricula', models.FloatField()),
                ('valor_matricula', models.FloatField()),
                ('valor_final_matricula', models.FloatField()),
                ('data_matricula', models.DateField()),
                ('data_primeira_mensalidade', models.DateField()),
                ('numero_parcelas', models.IntegerField()),
                ('valor_mensalidade', models.FloatField()),
                ('desconto_mensalidade', models.FloatField()),
                ('valor_final_mensalidade', models.FloatField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.aluno')),
            ],
        ),
    ]
