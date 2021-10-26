from django.contrib import admin
from django.db import models
from django.db.models.query_utils import select_related_descend
from django.http.response import HttpResponse
from .models import Pessoa, Cargos, Pedido
from django_object_actions import DjangoObjectActions
# Register your models here.

class PedidoInline(admin.TabularInline):
    readonly_fields = ('nome', 'quantidade', 'descricao')
    list_display = ('nome', 'quantidade', 'descricao')
    model = Pedido
    extra = 0

@admin.register(Pessoa)
class PessoaAdmin(DjangoObjectActions, admin.ModelAdmin):
    inlines = [PedidoInline]
    list_display = ('get_foto', 'nome', 'email', 'senha', 'nome_completo')
    #readonly_fields = ('senha', 'cargo')
    search_fields = ('nome','senha')
    list_filter = ('cargo',)
    list_editable = ('email',)

    def mostra_pessoa(self, request, pessoa):
        pessoa1 = Pessoa.objects.all(pessoa = pessoa)
        return HttpResponse(pessoa1)

    mostra_pessoa.label = "mostra pessoa"
    change_actions = ("mostra_pessoa", )



admin.site.register(Cargos)

