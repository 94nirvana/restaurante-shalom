from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField("Data de Criacao", auto_now_add=True)
    modificado = models.DateField("Data de Atualização", auto_now=True)
    ativo = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True


class Cliente(Base):
    nome = models.CharField("Nome", max_length=100)
    quantidade = models.DecimalField("Quantidade", decimal_places=0, max_digits=3)
    codigo = models.DecimalField("Codigo", decimal_places=0, max_digits=4)
    preferencia = models.CharField("Preferencia", max_length=10)

    def __str__(self):
        return f'Cliente: {self.nome} mesa para {self.quantidade} pessoas.'


def cliente_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(cliente_pre_save, sender=Cliente)


class Transferencia(Base):
    codigo = models.CharField("Codigo", max_length=4)
    destino = models.CharField("Destino", max_length=4)

    def __str__(self):
        return f'Transferencia: {self.codigo} - {self.destino}'


def transferencia_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.destino)


signals.pre_save.connect(transferencia_pre_save, sender=Transferencia)
