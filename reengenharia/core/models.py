from django.db import models

class Profissional(models.Model):
     nome=models.CharField(max_length=255)
class Atividade(models.Model):
     nome=models.CharField(max_length=255)
class Equipamento(models.Model):
     nome=models.CharField(max_length=255)
class Agendamento (models.Model):
     nome=models.CharField(max_length=255)
class Banco(models.Model):
     nome=models.CharField(max_length=255)
class Usuario(models.Model):
     nome=models.CharField(max_length=255)
class Aluno(models.Model):
    MASCULINO='M'
    FEMININO='F'
    sexo_choices=[
        [MASCULINO,'MASCULINO'],
        [FEMININO,'FEMININO'],
    ]
    nome=models.CharField(max_length=255)
    nascimento=models.DateField()
    sexo=models.CharField(choices=sexo_choices,max_length=255)
    ativo=models.BooleanField(default=True)
    fone=models.CharField(max_length=255)
    celular=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    cidade=models.CharField(max_length=255)
    uf=models.CharField(max_length=2)
    cep=models.CharField(max_length=255)
    rua=models.CharField(max_length=255)
    numero=models.CharField(max_length=255)
    bairro=models.CharField(max_length=255)

class Produto(models.Model):
     nome=models.CharField(max_length=255)
     valor=models.FloatField()

class Venda(models.Model):
    PRAZO='PRAZO'
    A_VISTA='À VISTA'
    pagamento_choices=[
        [PRAZO,'PRAZO'],
        [A_VISTA,'A_VISTA'],
    ]
    nome=models.CharField(max_length=255)
    produto=models.ManyToManyField('Produto')
    aluno=models.ForeignKey('Aluno',on_delete=models.DO_NOTHING,null=True,blank=True)
    forma_pagamento=models.CharField(choices=pagamento_choices,max_length=255)


