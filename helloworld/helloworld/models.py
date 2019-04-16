from django.db import models


class Funcionario(models.Model):

    numero= models.CharField( 
     max_length=255, 
     null=False, 
     blank=False 
    )
    
    vendedor = models.CharField( 
     max_length=25, 
     null=False, 
     blank=False 
    )

    data = models.CharField(
     max_length=11, 
     null=False, 
     blank=False 
    )

    nome = models.CharField( 
     max_length=255, 
     null=False, 
     blank=False 
    )

    NfDeOrigem = models.CharField(
     max_length=5, 
     null=False, 
     blank=False 
    )

    NfDeEntrada = models.PositiveIntegerField( 
      null=False, 
     blank=False 
    )

    NfDeSAida = models.PositiveIntegerField( 
     null=False, 
     blank=False
    )

    efeito = models.PositiveIntegerField( 
      null=False, 
      blank=False 
    )

    NumeroConserto = models.PositiveIntegerField( 
     null=False, 
     blank=False 
    )

    transpotadora = models.CharField( 
     max_length=255, 
     null=False, 
     blank=False 
    )

    CustoColeta = models.DecimalField( 
     max_digits=8, 
     decimal_places=2, 
     null=False,
     blank=False 
    )

    CustoIda = models.DecimalField( 
     max_digits=8, 
     decimal_places=2, 
     null=False, 
     blank=False
    )

    CustoVenda = models.DecimalField( 
     max_digits=8, 
     decimal_places=2, 
     null=False, 
     blank=False 
    )

    objetos = models.Manager()

  