from django.contrib import admin

from .models import *


class ProdutoVendaInlineAdmin(admin.TabularInline):
    model = ProdutoVenda
    extra = 1


class MatriculaAtividadeaInlineAdmin(admin.TabularInline):
    model = MatriculaAtividade
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    inlines = [ProdutoVendaInlineAdmin]


class AlunoAdmin(admin.ModelAdmin):
    fieldsets = [
        ['Dados pessoais', {'fields': [
            'nome',
            'nascimento',
            'sexo',
            'ativo',
            'fone',
            'celular',
            'email',
            'cidade',
            'uf',
            'cep',
            'rua',
            'numero',
            'bairro',
        ], }],
        ['Questionário', {'fields': [
            'plano_saude',
            'pratica_outro_esporte',
            'por_que_academia',

        ]}]
    ]


class MatriculaAdmin(admin.ModelAdmin):
    inlines = [MatriculaAtividadeaInlineAdmin]


admin.site.register(Profissional)
admin.site.register(Atividade)
admin.site.register(Equipamento)
admin.site.register(Agendamento)
admin.site.register(Banco)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Produto)
admin.site.register(ProdutoVenda)
admin.site.register(LocalAtividade)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Matricula, MatriculaAdmin)
