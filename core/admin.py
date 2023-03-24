from django.contrib import admin
from .models import Cliente, Transferencia


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "quantidade", "codigo", "preferencia", "criado", "modificado", "ativo")


@admin.register(Transferencia)
class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "destino")
