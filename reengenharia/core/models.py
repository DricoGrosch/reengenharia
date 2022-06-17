from django.db import models


class Profissional(models.Model):
    nome = models.CharField(max_length=255)


class LocalAtividade(models.Model):
    nome = models.CharField(max_length=255)


class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    local = models.ForeignKey('LocalAtividade', on_delete=models.DO_NOTHING)
    dia_semana = models.CharField(max_length=255)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    professor = models.ForeignKey('Profissional', on_delete=models.DO_NOTHING)
    equipamentos = models.ManyToManyField('Equipamento')

    def __str__(self):
        return f'{self.nome} | {self.local.nome} | {self.dia_semana} | {self.hora_inicio} | {self.hora_fim}| {self.professor.nome}'


class Matricula(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.DO_NOTHING)
    data_exame = models.DateField()
    validade_exame = models.DateField()
    inicio_contrato = models.DateField()
    vencimento_contrato = models.DateField()
    valor_pre_contrato = models.FloatField()
    pagamento_pre_contrato = models.FloatField()
    desconto_matricula = models.FloatField()
    valor_matricula = models.FloatField()
    valor_final_matricula = models.FloatField()
    data_matricula = models.DateField()
    data_primeira_mensalidade = models.DateField()
    numero_parcelas = models.IntegerField()
    valor_mensalidade = models.FloatField()
    desconto_mensalidade = models.FloatField()
    valor_final_mensalidade = models.FloatField()


class MatriculaAtividade(models.Model):
    matricula = models.ForeignKey('Matricula', on_delete=models.DO_NOTHING)
    atividade = models.ForeignKey('Atividade', on_delete=models.DO_NOTHING)


class Equipamento(models.Model):
    nome = models.CharField(max_length=255)


class Banco(models.Model):
    nome = models.CharField(max_length=255)


class Usuario(models.Model):
    nome = models.CharField(max_length=255)


class Aluno(models.Model):
    MASCULINO = 'M'
    FEMININO = 'F'
    sexo_choices = [
        [MASCULINO, 'MASCULINO'],
        [FEMININO, 'FEMININO'],
    ]
    nome = models.CharField(max_length=255)
    nascimento = models.DateField()
    sexo = models.CharField(choices=sexo_choices, max_length=255)
    ativo = models.BooleanField(default=True)
    fone = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    #     tab2
    plano_saude = models.CharField(max_length=255, null=True, blank=True)
    pratica_outro_esporte = models.CharField(max_length=255, null=True, blank=True)
    por_que_academia = models.CharField(max_length=255, null=True, blank=True, choices=[
        ['APRENDER_A_NADAR', 'APRENDER A NADAR'],
        ['BRONQUITE', 'APRENDER A NADAR'],
        ['COLUNA', 'APRENDER A NADAR'],
        ['OBESIDADE', 'APRENDER A NADAR'],
        ['TREINAR', 'APRENDER A NADAR'],
        ['MANTER_A_FORMA', 'APRENDER A NADAR'],
        ['APRENDER_A_NADAR', 'APRENDER A NADAR'],
    ])
    como_ficou_sabendo = models.CharField(max_length=255, null=True, blank=True)


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.FloatField()


class Venda(models.Model):
    PRAZO = 'PRAZO'
    A_VISTA = 'À VISTA'
    pagamento_choices = [
        [PRAZO, 'PRAZO'],
        [A_VISTA, 'À VISTA'],
    ]
    aluno = models.ForeignKey('Aluno', on_delete=models.DO_NOTHING, null=True, blank=True)
    forma_pagamento = models.CharField(choices=pagamento_choices, max_length=255)


class ProdutoVenda(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.DO_NOTHING)
    venda = models.ForeignKey('Venda', on_delete=models.DO_NOTHING)
    quantidade = models.FloatField()
