from helloworld.models import Funcionario
from django import forms


# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereFuncionarioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
            'numero',
            'data',
            'nome',
            'NfDeOrigem',
            'NfDeEntrada',
            'NfDeSAida',
            'efeito',
            'NumeroConserto',
            'vendedor',
            'transpotadora',
            'CustoColeta',
            'CustoIda',
            'CustoVenda',
        ]
