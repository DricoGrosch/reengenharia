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


class ProdutoVendaAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


class AlunoAdmin(admin.ModelAdmin):
    fieldsets = [
        ['Dados pessoais', {'fields': [
            ('nome'),
            ('nascimento',
             'sexo',
             'fone',),
            ('celular',
             'email',),
            ('cidade',
             'uf',
             'cep',),
            ('rua',
             'numero',
             'bairro',),
            'ativo',

        ], }],
        ['Questionário', {'fields': [
            'plano_saude', 'pratica_outro_esporte', 'por_que_academia',

        ]}]
    ]


class MatriculaAdmin(admin.ModelAdmin):
    inlines = [MatriculaAtividadeaInlineAdmin]
    fields = (
        (
            'aluno',
            'data_exame',
            'validade_exame',
        ),
        (
            'inicio_contrato',
            'vencimento_contrato',
            'valor_pre_contrato',
            'pagamento_pre_contrato',
            'valor_matricula',
            'desconto_matricula',
            'valor_final_matricula',
        ),
        (
            'data_matricula',
            'data_primeira_mensalidade',
            'numero_parcelas',
            'valor_mensalidade',
            'desconto_mensalidade',
            'valor_final_mensalidade',

        )
    )


admin.site.register(Profissional)
admin.site.register(Atividade)
admin.site.register(Equipamento)
admin.site.register(Banco)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Produto)
admin.site.register(ProdutoVenda, ProdutoVendaAdmin)
admin.site.register(LocalAtividade)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Matricula, MatriculaAdmin)
