from django.db import models
from produto.models import Produto
# Create your models here.

class MemoriaRam(models.Models):
    nome = models.CharFiled(max_length=30)
    tamanho = models.PositiveSmallIntegerField()
    produto = models.ForengKey(Produto, on_delete=models.CASCADE)