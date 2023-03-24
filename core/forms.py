from django import forms
from .models import Cliente, Transferencia


class ClienteForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    quantidade = forms.DecimalField(label="Pessoas", max_digits=3)
    codigo = forms.DecimalField(label="Codigo", max_digits=4)
    preferencia = forms.CharField(label="Preferencia", max_length=10)


class TransferenciaForm(forms.Form):
    codigo = forms.CharField(label="Codigo", max_length=4)
    destino = forms.CharField(label="Destino", max_length=4)


class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'quantidade', 'codigo', 'preferencia']


class TransferenciaModelForm(forms.ModelForm):
    class Meta:
        model = Transferencia
        fields = ['codigo', 'destino']
